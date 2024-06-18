from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/new/', views.faq_create, name='faq_create'),
    path('faq/<int:pk>/edit/', views.faq_update, name='faq_update'),
    path('faq/<int:pk>/delete/', views.faq_delete, name='faq_delete'),
]
