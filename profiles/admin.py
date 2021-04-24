from django.contrib import admin
from .models import Client,Company
from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.register(Client)
admin.site.register(Company)
# Register your models here.
