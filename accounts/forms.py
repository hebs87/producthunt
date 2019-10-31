from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create a new form object
class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    '''
    Form used to create and register a new user
    '''
    # Username
    username = forms.CharField(label='Username',
                               min_length=6,
                               max_length=15,
                               widget=forms.TextInput(),
                               required=True)
    password1 = forms.CharField(label="Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)
    # Confirm password with a label
    password2 = forms.CharField(label="Repeat Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
