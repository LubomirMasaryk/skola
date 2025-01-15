from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.list_knihy, name='index'),
    path('knihy/', views.list_knihy, name='list_knihy'),
    path('autori/', views.list_autori, name='list_autori'),
    path('vydavatelia/', views.list_vydavatelia, name='list_vydavatelia'),
    path('miesta/', views.list_miesta, name='list_miesta'),
]