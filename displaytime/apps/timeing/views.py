from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.now().date().strftime('%b %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date' : date},
            {'time' : time},
        ]
    }
    return render(request, 'templates.html', context)

# Create your views here.
