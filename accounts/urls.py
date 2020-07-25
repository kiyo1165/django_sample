from django.urls import path
from . import views

appname= 'accounts'

urlpatterns = [
    path('sigunup/', views.SignupView.as_view(), name='sigunup'),
]