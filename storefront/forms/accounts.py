from django import forms

class RegistrationForm(forms.Form):
    """The basic account registration form"""
    title = forms.Char
    email
    password1
    password2
    name



