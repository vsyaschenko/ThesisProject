from django.contrib import admin
from django.urls import path

from .views import index, by_section, by_process

urlpatterns = [
    path('', index, name='index'),
    path('section/<int:section_id>/', by_section, name='by_section'),
    path('process/<int:process_id>/', by_process, name='by_process'),
]