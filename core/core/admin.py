from django.contrib import admin
from .models import Person, Event, Registration

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Registration)