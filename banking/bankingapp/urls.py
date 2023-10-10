from django.urls import path, include
from . import views
app_name='bankingapp'
urlpatterns = [
    path('',views.home,name='home')

]
