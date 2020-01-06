from django.urls import path

from .views import index, by_selection

urlpatterns = [
    path('', index, name='index'),
    path('<int:id_selection>/', by_selection, name='by_selection'),
]
