from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('first/',views.first, name='first'),
    path('second/',views.second, name='second'),
    path('third/',views.third, name='third'),
]
