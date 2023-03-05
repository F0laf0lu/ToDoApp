from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
    path('edit/<int:pk>/', views.update_todo, name='edit')
]

