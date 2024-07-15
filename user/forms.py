from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 100, required = True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)


