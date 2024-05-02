# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_page, name='attendance_page'),
]
