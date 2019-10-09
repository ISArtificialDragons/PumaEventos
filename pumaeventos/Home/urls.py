from django.urls import path

from . import views

urlpatterns = [
    #Home page
    path('', views.home_page, name='home_page'),
]
