from django.contrib.auth import logout
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


def no_authentication_required(funk):
    def wrapped_funk(request,*args,**kwargs):
        if request.user.is_authenticated:
            logout(request)
        return funk(request,*args,**kwargs)

    return wrapped_funk


def authentication_required(funk):
    def wrapped_funk(request,*args,**kwargs):
        if request.user.is_authenticated:
            return funk(request,*args,**kwargs)
        return HttpResponseRedirect(reverse('login'))

    return wrapped_funk

def company_required(funk):
    def wrapped_funk(request,*args,**kwargs):
        if request.user.is_company:
            return funk(request,*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('main_page'))

    return wrapped_funk


def client_required(funk):
    def wrapped_funk(request, *args, **kwargs):
        if request.user.is_client:
            return funk(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('main_page'))

    return wrapped_funk

def id_check_for_user_change(funk):
    def wrapped_funk(request,*args,**kwargs):
        user=request.user
        if user.is_client:
            if user.client.id==kwargs['pk']:
                return funk(request,*args,**kwargs)
            else: raise PermissionDenied()
        elif user.is_company:
            if user.company.id==kwargs['pk']:
                return funk(request, *args, **kwargs)
            else: raise PermissionDenied()

    return wrapped_funk

def id_check_for_vacancy_change(funk):
    def wrapped_funk(request,*args,**kwargs):
        user = request.user
        if user.is_client:
            raise PermissionDenied()
        elif user.is_company:
            for vacancy in user.company.vacancies_of_company.all():
                if vacancy.id == kwargs['pk']:
                    return funk(request, *args, **kwargs)
            raise PermissionDenied()

    return wrapped_funk

