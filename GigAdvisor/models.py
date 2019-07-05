from django.db import models

class Platform(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    bestplatform = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='platform')

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
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

