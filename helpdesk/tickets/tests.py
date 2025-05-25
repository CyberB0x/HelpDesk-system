from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Ticket, Message

class HelpdeskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_ticket_creation(self):
        response = self.client.post(reverse('create_ticket'), {
            'title': 'Test Ticket',
            'description': 'Test Description',
            'status': 'open'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ticket.objects.count(), 1)
        ticket = Ticket.objects.first()
        self.assertEqual(ticket.title, 'Test Ticket')
        self.assertEqual(ticket.user, self.user)

    def test_ticket_detail_view(self):
        ticket = Ticket.objects.create(
            user=self.user,
            title='View Test',
            description='Test Desc'
        )
        response = self.client.get(reverse('ticket_detail', args=[ticket.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test')

    def test_add_message_to_ticket(self):
        ticket = Ticket.objects.create(
            user=self.user,
            title='Message Ticket',
            description='Initial'
        )
        response = self.client.post(reverse('ticket_detail', args=[ticket.id]), {
            'text': 'This is a reply message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ticket.messages.count(), 1)
        message = ticket.messages.first()
        self.assertEqual(message.text, 'This is a reply message')
        self.assertEqual(message.sender, self.user)

    def test_redirect_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse('create_ticket'))
        self.assertRedirects(response, '/accounts/login/?next=/tickets/create/')

    def test_ticket_report_view(self):
        # Создаем заявку со статусом 'resolved'
        Ticket.objects.create(
            title='T1',
            description='Desc 1',
            status='resolved',
            user=self.user
        )

        # Создаем заявку со статусом 'closed'
        Ticket.objects.create(
            title='T2',
            description='Desc 2',
            status='closed',
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('ticket_report'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Решено заявок')
        self.assertContains(response, '2')
