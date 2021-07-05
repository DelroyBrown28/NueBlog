from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control mb-3',
               'placeholder' : 'Username',
               'id' : 'login-username',}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Password',
            'id' : 'login-pwd',}
    ))
    
    
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=40, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required' : 'Sorry, you must enter an email address to register'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',)
        
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username
    
    def cleaned_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your passwords do not match, please re-check and try again.')
        return cd['repeat_password']
    
    def cleaned_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use. Please try another address.')
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['repeat_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
    
    
        