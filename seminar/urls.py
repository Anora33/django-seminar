from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('korea/', views.korea, name='korea'),
    path('seminar/', views.seminar_detail, name='seminar_detail'),
    path('contact/', views.contact, name='contact'),
]