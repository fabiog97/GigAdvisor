from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    avatar = models.ImageField(blank=True, default='avatar/default.png', upload_to='avatar/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True)
    cognome = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    residenza = models.CharField(max_length=50, blank=True)
    sesso = models.CharField(max_length=10, blank=True)
    titolo_di_studio = models.CharField(max_length=100, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

class Platform(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    bestplatform = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='platform')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.nome

class Recensioni(models.Model):
    data = models.DateTimeField('date published', auto_now=True)
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=2000)
    value1 = models.IntegerField(default=0)
    value2 = models.IntegerField(default=0)
    value3 = models.IntegerField(default=0)
    value4 = models.IntegerField(default=0)
    luogo =  models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo



