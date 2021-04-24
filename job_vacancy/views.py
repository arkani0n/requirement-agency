from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView,TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import classonlymethod
from profiles.models import Company, Client

from .models import JobVacancy
from . import forms


class VacancyCreate(CreateView):
    model = JobVacancy
    form_class = forms.VacancyForm
    template_name = 'job_vacancy/vacancy_create_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('vacancy_list')


class VacancyUpdate(UpdateView):
    model = JobVacancy
    template_name = 'job_vacancy/vacancy_update_form.html'
    form_class = forms.VacancyUpdateForm

    @classonlymethod
    def as_view(cls, **initkwargs):
        self = cls(**initkwargs)
        view = super(VacancyUpdate, cls).as_view(**initkwargs)
        return view

    def get_success_url(self):
        return reverse('vacancy_detail', args=[self.kwargs['pk']])


class VacancyDetail(DetailView):
    model = JobVacancy
    context_object_name = 'vacancy'
    template_name = 'job_vacancy/vacancy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class VacancyList(ListView):
    model = JobVacancy
    context_object_name = 'vacancy_list'
    template_name = 'job_vacancy/vacancy_list.html'
    extra_context = {'category_choises': JobVacancy.CATEGORY_CHOICES}
    paginate_by = 10
    def get_queryset(self):
        object_list=super(VacancyList, self).get_queryset()
        object_list=object_list.filter(is_active=True)
        return object_list


class CompaniesVacancyList(VacancyList):

    def get_queryset(self):
        object_list= JobVacancy.objects.filter(company_id=Company.objects.get(id=self.kwargs['pk']))
        return object_list


class MarkedVacanciesList(VacancyList):

    def get_queryset(self):
        object_list = super(MarkedVacanciesList, self).get_queryset()
        object_list=object_list.filter(marked_by_client=Client.objects.get(id=self.kwargs['pk']))
        return object_list


class SearchFilteredVacancyList(VacancyList):

    def get_queryset(self):
        object_list=super(SearchFilteredVacancyList, self).get_queryset()

        self.category_choice=self.request.GET.get('job_category')
        self.search_input=self.request.GET.get('search_input')
        if self.category_choice!='all':
            object_list=object_list.filter(category=self.category_choice)
        if self.search_input:
            object_list=object_list.filter(title__icontains=self.search_input)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(SearchFilteredVacancyList, self).get_context_data()
        context['user_choice'] = self.category_choice
        context['search_input']=self.search_input
        return context


class VacancyDelete(DeleteView):
    model = JobVacancy
    template_name = 'job_vacancy/vacancy_delete_confirm.html'

    def get_success_url(self):
        return reverse('vacancy_list')

def add_to_marked(request, pk):
    post = request.POST
    client = Client.objects.get(id=post.get('client_id'))
    vacancy = JobVacancy.objects.get(id=pk)
    vacancy.marked_by_client.add(client)
    return HttpResponseRedirect(reverse('vacancy_detail', args=[pk]))


def delete_from_marked(request, pk):
    post = request.POST
    client = Client.objects.get(id=post.get('client_id'))
    vacancy = JobVacancy.objects.get(id=pk)
    vacancy.marked_by_client.remove(client)
    return HttpResponseRedirect(reverse('vacancy_detail', args=[pk]))


class VacancyClientCVs(TemplateView):

    template_name = 'job_vacancy/client_cvs.html'

    def get_query_set(self):
        vacancy=JobVacancy.objects.get(id=self.kwargs['pk'])
        clients=vacancy.marked_by_client.all()
        print(clients)
        return clients


    def get_context_data(self, **kwargs):
        context=super(VacancyClientCVs, self).get_context_data()
        context['base_url']=self.request.META['HTTP_HOST']
        clients=self.get_query_set()
        context['clients']=clients
        return context

