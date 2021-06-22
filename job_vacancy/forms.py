from django.forms import ModelForm
from django.db import transaction

from .models import JobVacancy
from profiles.models import Company


class VacancyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    @transaction.atomic
    def save(self, commit=True):
        vacancy = super().save(commit=False)
        company_id = self.request.user.company.id
        company = Company.objects.get(id=company_id)
        vacancy.company_id = company
        vacancy.save()
        return vacancy

    class Meta:
        model = JobVacancy
        fields = ['title', 'category', 'description', 'short_description', 'needed_skills', 'salary', 'city',
                  'is_active']


class VacancyUpdateForm(ModelForm):
    class Meta:
        model = JobVacancy
        fields = ['title', 'category', 'short_description', 'description', 'needed_skills', 'salary', 'city',
                  'is_active']
