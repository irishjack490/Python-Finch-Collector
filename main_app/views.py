from django.shortcuts import render
from .models import Finch

# finches = [

#     {'breed': 'Zebra Finch', 'scientific_name': 'Taeniopygia guttata', 'personality': 'does not wantt to be handled', 'age_span' :'10'},
#     {'breed': 'Gouldian Finch', 'scientific_name' : 'Chloebia Gouldiae', 'personality' : 'Lovely to watch, not to hold', 'age_span' : '4'}

# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all() # retrieve all finches
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})