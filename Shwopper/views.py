from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.forms.util import ErrorList         #Used to add cusom error in form
from urllib2 import urlopen                     #Used to check that given url is valid
from Shwopper.shwoppertools.forms import ShwopLinkForm   #Custom form for email and link
from Shwopper.shwoppertools import cryptolink, shwopConverter    #Contains tools to convert urls into shortened links

from models import ShwopLink

def index(request):
    if request.method == 'POST':
        shwopForm = ShwopLinkForm(request.POST)
        if shwopForm.is_valid():
            email = shwopForm.cleaned_data['email']
            link = shwopForm.cleaned_data['link']
#            try:
            code = urlopen(link).code
            if ( code / 100 < 4):
                return processShwopLink(request, email, link)
#            except Exception: #Catch exception if link does not exist
#                pass

            errors = shwopForm._errors.setdefault("link", ErrorList())
            errors.append(u"Link provided does not exist")

    else:
        shwopForm = ShwopLinkForm()

    return render(request, 'Shwopper/index.html', {
        'shwopForm': shwopForm,
        })

def processShwopLink(request, email, link):
    #registerUser(email)
    shwopLink = shwopConverter.convertIntoAffiliate(link)

    if shwopLink:
        shwopLinkInstance = ShwopLink.objects.create(shwoplink=shwopLink, isaffiliate=True)
        shwopLinkInstance.save()
        index = shwopLinkInstance.shwoplinkid
        shwopCode = cryptolink.encrypt(index)

        return render(request, 'Shwopper/shwopLinkSuccess.html',  {'shwopCode' : shwopCode})
    else:
        shwopLinkInstance = ShwopLink.objects.create(shwoplink=link, isaffiliate=False)
        shwopLinkInstance.save()
        index = shwopLinkInstance.shwoplinkid
        shwopCode = cryptolink.encrypt(index)

        return render(request, 'Shwopper/shortLinkSuccess.html',  {'shwopCode' : shwopCode})




def processRequest(request, code=""):
    index = cryptolink.decrypt(code)

    try:
        shwopLinkInstance = ShwopLink.objects.get(pk=index)
        shwopLinkInstance.visitcount = shwopLinkInstance.visitcount + 1 #Recording visit count of link
        shwopLinkInstance.save()

        return HttpResponsePermanentRedirect(shwopLinkInstance.__str__())

    except ShwopLink.DoesNotExist:
        return render(request, 'Shwopper/404.html')