from django.db import models
from django.urls import reverse

class JobVacancy(models.Model):

    CATEGORY_CHOICES=(
        ('python','Python'),
        ('java','Java'),
        ('qa','QA'),
        ('qa_automation','QA Automation'))

    is_active=models.BooleanField(default=True,help_text='* If active will appear in search results')
    title = models.CharField(max_length=70)
    short_description=models.CharField(max_length=200,default='No short description')
    description = models.TextField()
    needed_skills = models.TextField()
    salary = models.IntegerField(blank=True,help_text='*Per month')
    city = models.CharField(max_length=40)
    company_id = models.ForeignKey('profiles.Company', on_delete=models.CASCADE,related_name='vacancies_of_company')
    publish_dat = models.DateField(auto_now=True)
    marked_by_client=models.ManyToManyField('profiles.Client',related_name='marked_vacancies')
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    def get_absolute_url(self):
        return reverse('vacancy_detail',self.id)

    def __str__(self):
        return self.title
