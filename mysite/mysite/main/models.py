from django.db import models


class UserNet(models.Model):
    imie = models.CharField(max_length=150)
    nazwisko = models.CharField(max_length=200)
    zdj = models.ImageField(default=0)
    git_hub = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    kolejnosc = models.IntegerField(default=98)

    def __str__(self):
        return self.imie

    class Meta:
        app_label = "main"
        ordering = ['kolejnosc']


class Comunication(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.EmailField()
    tekst = models.TextField(max_length=1000)

    def __str__(self):
        return self.email

    class Meta:
        app_label = "main"

