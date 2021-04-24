from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.urls import reverse


class AccountManager(BaseUserManager):

    def create_user(self,email,password=None):

        user= self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None):
        user= self.create_user(
            email=self.normalize_email(email),
            password=password
            )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class AbstractAccount(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True, blank=True)
    is_company=models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = AccountManager()
    def __str__(self):
        return 'Client' if self.is_client else 'Company'

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True


class Client(models.Model):
    user = models.OneToOneField(AbstractAccount,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True)
    about = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    country = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=40,blank=True)
    cv = models.FileField(blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('client_detail',args=[self.id])


class Company(models.Model):
    user = models.OneToOneField(AbstractAccount,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=40,unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True)
    about = models.TextField(blank=True)
    web_site = models.URLField(blank=True)
    massages = models.ManyToManyField('Client', through='ChatMassage')

    def __str__(self):
        return f'{self.company_name}'

    def get_absolute_url(self):
        return reverse('company_detail',args=[self.id])




class ChatMassage(models.Model):
    send_time = models.DateTimeField(auto_now=True)
    text = models.TextField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE,related_name='company_id')
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE,related_name='client_id')

# Create your models here.
