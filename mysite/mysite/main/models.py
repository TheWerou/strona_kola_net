from django.db import models


class UserNet(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    zdj = models.ImageField(width_field=600, height_field=600)
    git_hub = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()
    kolejnosc = models.SmallIntegerField()


class Comunication(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.EmailField()
    tekst = models.TextField(max_length=1000)


