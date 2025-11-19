from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "ticket1": "User cannot login to the system.",
    }
    return render(request, "tickets/tickets.html", context)