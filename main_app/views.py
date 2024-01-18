from django.shortcuts import render

finches = [

    {'breed': 'Zebra Finch', 'scientific_name': 'Taeniopygia guttata', 'personality': 'does not wnat to be handled'},
    {'breed': 'Gouldian Finch', 'scientific_name' : 'Chloebia Gouldiae', 'personality' : 'Lovely to watch, not to hold'}

]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })