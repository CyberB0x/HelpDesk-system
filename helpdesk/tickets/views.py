from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now, timedelta
from django.contrib.auth.decorators import login_required
from .models import Ticket, Message
from .forms import TicketForm, MessageForm

def report_view(request):
    last_30_days = now() - timedelta(days=30)
    resolved_tickets = Ticket.objects.filter(status='resolved', created_at__gte=last_30_days)
    total_resolved = resolved_tickets.count()

    return render(request, 'tickets/report.html', {
        'resolved_tickets': resolved_tickets,
        'total_resolved': total_resolved
    })

@login_required
def ticket_detail_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    messages = ticket.messages.all().order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.ticket = ticket
            msg.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()

    return render(request, 'tickets/ticket_detail.html', {
        'ticket': ticket,
        'messages': messages,
        'form': form,
    })


@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})


@login_required
def ticket_list_view(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})