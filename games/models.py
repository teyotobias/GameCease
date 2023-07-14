from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_released = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # title_cover = models.ImageField(upload_to='game_covers/')



    def __str__(self):
        return f'{self.title} ({self.id})'
    
    
    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.pk})