from django.urls import path
from . import views

urlpatterns = [
path('', views.usersettings, name='user-settings'),
]