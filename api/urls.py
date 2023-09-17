from django.urls import path
from . import views
from .views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('home', views.home, name='home'),
]