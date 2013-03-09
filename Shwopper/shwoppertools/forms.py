from django import forms

class ShwopLinkForm(forms.Form):
    email = forms.EmailField()
    link = forms.URLField()