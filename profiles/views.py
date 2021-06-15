from django.views.generic import DetailView,CreateView,UpdateView,TemplateView,ListView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from . import models,forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from job_vacancy.models import JobVacancy
from django.views.generic.list import MultipleObjectMixin


class RegisterView(TemplateView):
    template_name = 'profiles/register_choise_page.html'


class ClientCreate(CreateView):
    model = models.Client
    form_class = forms.ClientRegisterForm
    template_name = 'profiles/account_registration_form.html'

    def form_valid(self,form):
        print(form)
        client = form.save()
        login(self.request, client)
        return HttpResponseRedirect(reverse('main_page'))


class CompanyCreate(CreateView):
    model = models.Company
    form_class = forms.CompanyRegisterForm
    template_name = 'profiles/account_registration_form.html'

    def form_valid(self,form):
        company = form.save()
        login(self.request, company)
        return HttpResponseRedirect(reverse('main_page'))


class ClientUpdate(UpdateView):
    model=models.Client
    form_class = forms.ClientChangeForm
    template_name = 'profiles/client_update_form.html'


class CompanyUpdate(UpdateView):
    model=models.Company
    form_class = forms.CompanyChangeForm
    template_name = 'profiles/company_update_form.html'


class Login(LoginView):
    template_name = 'profiles/login.html'

    def get_success_url(self):
        return reverse('main_page')


class Logout(LogoutView):

    def get_next_page(self):
        return reverse('main_page')


class ClientDetail(DetailView):
    model=models.Client
    context_object_name = 'client'
    template_name = 'profiles/client_detail.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        context['base_url']=ip
        if ip == '127.0.0.1':
            context['port'] = self.request.META['SERVER_PORT']

        return context



class CompanyDetail(ListView):
    context_object_name = 'vacancies'
    template_name = 'profiles/company_detail.html'
    paginate_by = 3


    def get_queryset(self):
        self.queryset = JobVacancy.objects.filter(company_id_id=self.kwargs['pk'],is_active=True)
        self.queryset=super().get_queryset()
        return self.queryset

    def get_context_data(self, **kwargs):

        context = super(CompanyDetail, self).get_context_data()
        context['company'] = models.Company.objects.get(id=self.kwargs['pk'])
        return context


