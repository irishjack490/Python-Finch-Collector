from django.db import models

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    personality = models.TextField(max_length=150)
    age_span = models.IntegerField()

    def _str_(self):
        return self.breed


