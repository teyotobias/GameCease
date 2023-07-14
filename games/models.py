from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    age_restriction_choices = [
        ('E', 'Everyone'),
        ('T', 'Teen'),
        ('M', 'Mature')
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age_rectriction = models.CharField(max_length=1, choices=age_restriction_choices)
    year_released = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    title_cover = models.ImageField(upload_to='game_covers/')
    

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})