from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    personality = models.TextField(max_length=150)
    age_span = models.IntegerField()
    
    
def __str__(self):
    return f'{self.breed} ({self.id})'
    
  # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})


