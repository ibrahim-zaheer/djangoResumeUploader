 
from .views import HomeView,CandidateView

from django.urls import path
urlpatterns = [
     path('', HomeView.as_view(), name='home'),
    path('<int:pk>', CandidateView.as_view(), name='candidate'),
]
