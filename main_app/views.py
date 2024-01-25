from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Watercup
from .forms import FeedingForm
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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
       'finch': finch, 'feeding_form': feeding_form 
       })
#instantiate feeding form to be rendered in the template
    #feeding form is set to an instance of FeedingForm and then passed to detail.html
    #in the context along with finch 
   

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)
    

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


class WatercupDetail(DetailView):
   model = Watercup
