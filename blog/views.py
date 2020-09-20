from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
        "name": "Shashi Prajapati",
        "id": "46",
        "qualification": "Html, CSS, Python",
        "place": "Thane"
    },
    {
        "name": "Meet Thakar",
        "id": "64",
        "qualification": "Html, CSS, JS, Python",
        "place": "Mulund"
    },
    {
        "name": "Anshuman Tiwari",
        "id": "65",
        "qualification": "Html, CSS, JS, Python, Django, C, C++",
        "place": "Belapur"
    },
    {
        "name": "Vishnu",
        "id": "02",
        "qualification": "Html, CSS, Python",
        "place": "Thane"
    },
]


def home(request):
    # return HttpResponse("<h1>Hello World<h1>")
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, "blog/about.html", {'title': 'about'})


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    total = val1 + val2

    return render(request, "blog/about.html", {'total': total})
