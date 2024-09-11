from django.shortcuts import render
from django.http import HttpResponse
from .models import Visits
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world!")

def index(request):
    v = Visits.objects.first()
    v.count += 1
    v.save()
    context = {"num_visits": v.count}
    return render(request, 'index.html', context=context)