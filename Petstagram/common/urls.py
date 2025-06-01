from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
   path('', views.home_page, name='home-page'),

]