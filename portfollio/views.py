
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def index(request):
    portfolio=Project.objects.all()
    return render(request, 'portfolio/index.html', {'Project': portfolio})



