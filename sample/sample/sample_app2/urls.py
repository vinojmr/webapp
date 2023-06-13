from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:actor_id>/', views.details2, name='details2'),
    path('add/', views.add2, name='add2'),
    path('<int:actor_id>/update2/', views.update2, name='update2'),
]
