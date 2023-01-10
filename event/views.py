from django.shortcuts import render
from .models import Event

def home(request):
	events = Event.objects	
	return render(request,'event/home.html', {'events': events})