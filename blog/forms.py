from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs= {'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs= {'class':'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }
        widgets = {
            'username':forms.TextInput(attrs= {'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(label=('Username'),widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'),widget=forms.PasswordInput(attrs={'sutocomplete':'current-password', 'class':'form-control'}), strip=False)


class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','description']
        labels = {
            'title' : 'Article Title',
            'description': 'Article Description'
        }
        widgets = {
            'title': forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}),
            'description': forms.Textarea(attrs={'autofocus':True, 'class':'form-control'})
        }

