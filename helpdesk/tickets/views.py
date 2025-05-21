from django.shortcuts import render
from django.utils.timezone import now, timedelta
from .models import Ticket

def report_view(request):
    last_30_days = now() - timedelta(days=30)
    resolved_tickets = Ticket.objects.filter(status='resolved', created_at__gte=last_30_days)
    total_resolved = resolved_tickets.count()

    return render(request, 'tickets/report.html', {
        'resolved_tickets': resolved_tickets,
        'total_resolved': total_resolved
    })
