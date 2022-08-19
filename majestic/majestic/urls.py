from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cost/', views.cost, name='cost'),
    path('contacts/', views.contacts, name='contacts'),
]