from django.urls import path
from . import views
from .views import ApplicationCreateView,ApplicationDetailView,ApplicationUpdateView,ApplicationListView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('application/',  ApplicationCreateView.as_view(), name='application-create'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/update', ApplicationUpdateView.as_view(), name='application-update'),
    path('applications/', ApplicationListView.as_view(), name='main-applications'),
]
