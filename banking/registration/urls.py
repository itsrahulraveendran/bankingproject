from . import views
from django.urls import path

urlpatterns=[
    path('show_application_form/',views.show_application_form,name='show_application_form'),
    path('application_confirmation', views.application_confirmation, name='application_confirmation'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.home,name='home')
]