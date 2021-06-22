from django.urls import path
from . import views
from . import decorators

urlpatterns = [
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('client/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
    path('reg', decorators.no_authentication_required(views.RegisterView.as_view()), name='register'),
    path('client/reg', decorators.no_authentication_required(views.ClientCreate.as_view()), name='client_register'),
    path('company/reg', decorators.no_authentication_required(views.CompanyCreate.as_view()), name='company_register'),
    path('login', decorators.no_authentication_required(views.Login.as_view()), name='login'),
    path('client/change/<int:pk>',
         decorators.authentication_required(
             decorators.client_required(
                 decorators.id_check_for_user_change(views.ClientUpdate.as_view()))), name='client_update'),

    path('company/change/<int:pk>',
         decorators.authentication_required(
             decorators.company_required(
                 decorators.id_check_for_user_change(views.CompanyUpdate.as_view()))),
         name='company_update'),

    path('logout', views.Logout.as_view(), name='logout')

]
