from django.shortcuts import render
from django.http import HttpResponse
from .models import Visit
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world!")

def index(request):
    v = Visit(page="")
    if request.user.is_authenticated:
        v.username = request.user.username

    v.save()

    visitors = Visit.objects.filter(page="")
    context = {
        "num_visits" : visitors.count()
    }

    return render(request, "index.html", context)