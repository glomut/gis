from django.urls import path
from . import views
from .views import ApplicationView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('application/', ApplicationView.as_view(), name='application-create'),
]
