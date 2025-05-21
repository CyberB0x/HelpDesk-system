from django.urls import path
from .views import report_view

urlpatterns = [
    path('report/', report_view, name='ticket_report'),
]
