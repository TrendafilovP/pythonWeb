from django.urls import path
from petstagram.petstagram.common import views

urlpatterns = [
    path('', views.home, name='home')
]
