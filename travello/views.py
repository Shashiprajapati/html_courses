from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city that never sleeps"
    dest1.img = "destination_1.jpg"
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Punjab"
    dest2.desc = "Awesome foods"
    dest2.img = "destination_2.jpg"
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Manali"
    dest3.desc = "The snow world"
    dest3.img = "destination_3.jpg"
    dest3.price = 950
    dest3.offer = False

    dest4 = Destination()
    dest4.name = "Hyderabad"
    dest4.desc = "The snow world"
    dest4.img = "destination_4.jpg"
    dest4.price = 500
    dest4.offer = True

    # dests = [dest1, dest2, dest3, dest4]
    dests = Destination.objects.all()

    return render(request, "blog/index.html", {'dests': dests})
