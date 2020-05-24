from django.urls import path
from . import views
from .views import EducationView, ApplicationCreateView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('education/', EducationView.as_view(), name='education-create'),
    path('application/', ApplicationCreateView.as_view(), name='application-create'),
]
