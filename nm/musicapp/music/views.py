# music/views.py

from django.shortcuts import render
from .models import Song

def index(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})
