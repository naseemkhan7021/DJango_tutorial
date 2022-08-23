from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Flight, Passanger

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        "flights": Flight.objects.all(),
        "page_title": "Flight list"
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)  # flight id or  pk(primery key)
    return render(request, 'flights/flight.html', {
        "flight": flight,
        "passangers": flight.passangers.all(),
        "non_passangers" : Passanger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)
        # Finding the passenger id from the submitted form data
        passanger_id = int(request.POST["passanger"])
        # Finding the passenger based on the id
        passanger = Passanger.objects.get(pk=passanger_id)
        # Add passenger to the flight
        passanger.flights.add(flight)
        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
