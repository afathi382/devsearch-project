from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelFormOptions

from .models import Message, Profile



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['first_name' ,'email' ,'username' , 'password1', 'password2']



class profileform(ModelForm):
    class Meta:
        model= Profile
        fields= ['name', 'email', 'username', 'location', 'short_intro', 'bio', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']


class messageform(ModelForm):
    class Meta:
        model= Message
        fields= ['subject', 'email', 'body']

      
