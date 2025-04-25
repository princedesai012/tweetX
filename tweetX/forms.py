from django import forms
from .models import tweetX
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[MinLengthValidator(8)],
        help_text="At least 8 characters"
    )

class tweetXForm(forms.ModelForm):
    class Meta:
        model = tweetX
        fields = ['text', 'photo']
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')