from django.contrib import admin
from .models import JobVacancy


class VacancyAdmin(admin.ModelAdmin):
    list_filter = ('is_active',)
    list_display = ('title', 'company_id', 'is_active')


admin.site.register(JobVacancy, VacancyAdmin)
