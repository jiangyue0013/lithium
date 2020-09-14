from django.shortcuts import render

from .models import Team

def index(request):
    return render(request, 'team/index.html', context={'teams': Team.objects.all()})