from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from . import models


class ClientRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = models.AbstractAccount
        fields = ['email', 'password1', 'password2'
                  ]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = models.Client.objects.create(user=user)
        client.first_name = self.cleaned_data.get('first_name')
        client.last_name = self.cleaned_data.get('last_name')
        client.email = self.cleaned_data.get('email')
        client.save()
        return user


class CompanyRegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=60)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta(UserCreationForm.Meta):
        model = models.AbstractAccount
        fields = ['email', 'password1', 'password2'
                  ]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = models.Company.objects.create(user=user)
        company.company_name = self.cleaned_data.get('company_name')
        company.email = self.cleaned_data.get('email')
        company.phone_number = self.cleaned_data.get('phone_number')
        company.save()
        return user


class ClientChangeForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['image', 'first_name', 'last_name', 'email', 'phone_number',
                  'about', 'cv', 'skills', 'country', 'city']


class CompanyChangeForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['image', 'company_name', 'email', 'phone_number',
                  'about', 'web_site']
