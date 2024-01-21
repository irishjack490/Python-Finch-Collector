from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from django.urls import reverse

# finches = [

#     {'breed': 'Zebra Finch', 'scientific_name': 'Taeniopygia guttata', 'personality': 'does not wantt to be handled', 'age_span' :'10'},
#     {'breed': 'Gouldian Finch', 'scientific_name' : 'Chloebia Gouldiae', 'personality' : 'Lovely to watch, not to hold', 'age_span' : '4'}

# ]

# Create your views here.
def __str__(self):
   return f'{self.breed} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})

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

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__' #['breed', 'scientific_name', 'personality', 'age_span']
  success_url = '/finches'


class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'scientific_name', 'personality', 'age_span']
  success_url = '/finches'
  


class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'