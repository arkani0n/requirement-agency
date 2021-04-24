from django.contrib import admin
from django.urls import path, include
from . import views
from profiles import decorators

urlpatterns = [
    path('create', decorators.authentication_required(
        decorators.company_required(views.VacancyCreate.as_view())), name='vacancy_create'),
    path('change/<int:pk>', decorators.authentication_required(
        decorators.id_check_for_vacancy_change(
            views.VacancyUpdate.as_view())), name='vacancy_update'),
    path('<int:pk>', views.VacancyDetail.as_view(), name='vacancy_detail'),
    path('all', views.VacancyList.as_view(), name='vacancy_list'),
    path('all/<int:pk>', views.CompaniesVacancyList.as_view(), name='companys_vacancy_list'),
    path('all/marked/<int:pk>', views.MarkedVacanciesList.as_view(), name='clients_marked_vacancies_list'),
    path('all/filtered', views.SearchFilteredVacancyList.as_view(), name='search_filtered_vacancies_list'),
    path('<int:pk>/mark_add', views.add_to_marked, name='mark_vacancy'),
    path('<int:pk>/mark_delete', views.delete_from_marked, name='remove_marked_vacancy'),
    path('<int:pk>/delete', views.VacancyDelete.as_view(), name='vacancy_delete'),
    path('<int:pk>/cvs', decorators.authentication_required(
        decorators.company_required(
            decorators.id_check_for_vacancy_change(views.VacancyClientCVs.as_view()))), name='vacancy_see_cvs')
]
