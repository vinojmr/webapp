from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('celeb/', views.celebrity, name='celebrity'),
    path('celeb/<int:id>/', views.details, name='details'),
    path('celeb/add/', views.add, name='add'),
    path('celeb/<int:id>/update/', views.update, name='update'),
    path('celeb/<int:id>/delete/', views.delete, name='delete')

]
