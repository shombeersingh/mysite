from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard,name='home'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),# Add this
    path('payment/', views.record_payment, name='record_payment'), # New Route
]
