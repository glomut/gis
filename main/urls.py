from django.urls import path
from . import views
from .views import ApplicationCreateView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('application/',  ApplicationCreateView.as_view(), name='application-create'),
]
