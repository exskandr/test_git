from django.contrib import admin
from .models import Repair, ServiceClient, ServiceWork, TerminalClient

admin.site.register(Repair)
admin.site.register(ServiceWork)
admin.site.register(ServiceClient)
admin.site.register(TerminalClient)