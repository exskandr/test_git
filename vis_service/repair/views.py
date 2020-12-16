from django.shortcuts import render
from .models import Repair
import calendar
from datetime import datetime

# Create Calendar


# Create page

def index(request):
    conts = Repair.objects.all()
    c = calendar.HTMLCalendar()
    html_out = c.formatmonth(datetime.today().year, datetime.today().month)

    return render(request, "index.html", {'conts': conts, 'calendar': html_out})


def about(request):
    conts = Repair.objects.all()

    return render(request, "about.html", {'conts': conts})


