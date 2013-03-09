from django import forms

class ShwopLinkForm(forms.Form):
    email = forms.EmailField()
    email.required=False
    link = forms.URLField()