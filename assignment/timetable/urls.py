from django.contrib import admin
from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns = [
    path('',views.home, name='home'),
    path('examsetup',views.ExamSetup, name='examsetup'),
    path('examtime',views.ExamTime, name='examtime'),
    path('exam/delete/<int:id>', views.TimeDelete, name='TimeDelete'),
    path('admin_page',views.admin, name='admin_page'),
]
