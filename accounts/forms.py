from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    """
      Form for Registering new users
    """
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (
        self.fields['email'], self.fields['username'], self.fields['password1'], self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class AccountUpdateform(forms.ModelForm):
    """
      Updating User Info
    """

    class Meta:
        model = Account
        fields = ('email', 'username')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields
        """
        super(AccountUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['username']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' already in use." % username)


class AccountGeneralForm(forms.ModelForm):
    class Meta:
        model = Account

        fields = [
            'username',
            'first_name',
            'email',
            'company'
        ]


"""
class RegisterForm(forms.Form):

    username = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length = 20)
    confirm = forms.CharField(max_length = 20)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler Eşleşmedi!")

        values = {
            "username" : username,
            "email": email,
            "password" : password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        values = {
            "username": username,
            "password": password
        }
        return values
"""
"""
from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email',)

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})


class AccountAuthenticationForm(forms.ModelForm):

    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  Account
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):

        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

class AccountUpdateform(forms.ModelForm):

    class Meta:
        model  = Account
        fields = ('email', 'username')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):

        super(AccountUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' already in use." % username)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
"""