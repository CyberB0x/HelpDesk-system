from django.urls import path
from .views import create_ticket_view, ticket_detail_view, report_view

urlpatterns = [
    path('tickets/create/', create_ticket_view, name='create_ticket'),
    path('tickets/<int:ticket_id>/', ticket_detail_view, name='ticket_detail'),
    path('report/', report_view, name='ticket_report'),
]

