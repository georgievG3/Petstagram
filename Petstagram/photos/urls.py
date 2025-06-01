from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('add/', views.photo_add_view, name='add-photo'),
    path('<int:pk>', include([
        path('', views.photo_details_view, name='photos-details'),
        path('edit/', views.photo_edit_view, name='edit_photo'),
    ]))

]