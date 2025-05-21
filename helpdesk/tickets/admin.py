from django.contrib import admin
from .models import UserProfile, Ticket, Message

admin.site.register(UserProfile)
admin.site.register(Ticket)
admin.site.register(Message)

