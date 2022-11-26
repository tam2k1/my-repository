from django.urls import path
from . import views

urlpatterns = [
    path('',views.start),
    path('loaded/', views.userCommand, name='index')
]