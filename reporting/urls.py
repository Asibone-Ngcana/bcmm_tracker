from django.urls import path
from . import views

app_name = 'reporting'

urlpatterns = [
    path('', views.report_fault, name='report_fault'),
    path('track/<str:ref_id>/', views.track_report, name='track_report'),
]
