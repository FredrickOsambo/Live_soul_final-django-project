from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feedback
from .models import UserProfile
from .models import Article
from django.contrib.auth.forms import AuthenticationForm



class SignUpForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

# core/forms.py



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'age', 'gender']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
