from django.forms import ModelForm
from .models import Feeding
#this class form is instantiated in views.py
class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']