from . import views
from django.urls import path

urlpatterns = [
    path('',views.home2, name='home2'),
]