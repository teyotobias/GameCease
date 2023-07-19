from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_released = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    cover = models.ImageField(upload_to='images/', default='games/default.jpg')
    recommended = models.BooleanField(default=True)
    purchased = models.BooleanField(default=False)



    def __str__(self):
        return f'{self.title} ({self.id})'
    
    
    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.pk})
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    games_in_cart = models.ManyToManyField(Game, blank=True, related_name='users_with_game')
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    purchased_games = models.ManyToManyField(Game, blank=True, related_name='purchasers')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()    