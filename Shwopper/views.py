from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.forms.util import ErrorList         #Used to add cusom error in form
import urllib2                                  #Used to check that given url is valid
from Shwopper.shwoppertools.forms import ShwopLinkForm   #Custom form for email and link
from Shwopper.shwoppertools import cryptolink, shwopConverter    #Contains tools to convert urls into shortened links

#Used to create user
from accounts.models import MyProfile
from userena.models import UserenaSignup
from django.contrib.auth.models import User

from ShwopIt import settings as custom_userena_settings
from django.conf import settings
from django.core.mail import send_mail

from models import ShwopLink

def shwopBox(request, alertMessage = ""):
    if request.method == 'POST':
        shwopForm = ShwopLinkForm(request.POST)
        if shwopForm.is_valid():
            email = shwopForm.cleaned_data['email']
            link = shwopForm.cleaned_data['link']
            try:
                #urlrequest has to be used as some websites don't allow python to request data, sending a 404
                urlrequest = urllib2.Request(link, headers={'User-Agent' : "Shwop.It"} )
                code = urllib2.urlopen(urlrequest).code
                if ( code / 100 < 4):
                    return processShwopLink(request, email, link)
            except urllib2.HTTPError: #Catch exception if link does not exist
                pass
            except urllib2.URLError: #Catch exception if link does not exist
                pass

            alertMessage = "Link provided is not valid"

    else:
        shwopForm = ShwopLinkForm()

    return render(request, 'Shwopper/shwopBox.html', {
        'shwopForm': shwopForm,
        'alertMessage' : alertMessage
        })

def processShwopLink(request, email, link):
    user = None
    password = ""
    username = ""
    userCreated = False

    if request.user.is_authenticated():
        user = request.user.my_profile
    elif email:
        username = email.split('@')[0]
        try:
            user = User.objects.get(username=username).my_profile
        except User.DoesNotExist:
            password = User.objects.make_random_password()
            UserenaSignup.objects.create_user(username,
                                                email,
                                                password,
                                                not custom_userena_settings.USERENA_ACTIVATION_REQUIRED,
                                                custom_userena_settings.USERENA_ACTIVATION_REQUIRED)
            subject = "Welcome!"
            message = "Hello " + username + "! \n\n Your new username is: " + username + "\nYour new password is: '" + password + "'."
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email,])
            userCreated=True

    affiLink = shwopConverter.convertIntoAffiliate(link)
    shwopLinkInstance = ShwopLink.objects.create(   originallink=link,
                                                    affiliatelink=affiLink,
                                                    userref=user)
    shwopLinkInstance.save()
    index = shwopLinkInstance.shwoplinkid
    shwopCode = cryptolink.encrypt(index)

    return render(request, 'Shwopper/shwopLinkSuccess.html',  {'shwopCode' : shwopCode,
                                                               'affiLink' : affiLink,
                                                               'currUser' : user,
                                                                'userCreated': userCreated})




def processRequest(request, code=""):
    index = cryptolink.decrypt(code)

    try:
        shwopLinkInstance = ShwopLink.objects.get(pk=index)
        shwopLinkInstance.visitcount = shwopLinkInstance.visitcount + 1 #Recording visit count of link
        shwopLinkInstance.save()

        return HttpResponsePermanentRedirect(shwopLinkInstance.__str__())

    except ShwopLink.DoesNotExist:
        return render(request, 'Shwopper/404.html')