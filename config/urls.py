from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change_done/', views.PasswordChangeDoneView.as_view(),name='/password_change_done'),
]
