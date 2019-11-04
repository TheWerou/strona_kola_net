from django.db import models


class UserNet(models.Model):
    imie = models.CharField(max_length=150)
    nazwisko = models.CharField(max_length=200)
    zdj = models.ImageField(width_field=600, height_field=600)
    git_hub = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    kolejnosc = models.IntegerField(default=98)

    class Meta:
        app_label = "main"
        ordering = ['kolejnosc']
        db_table = "usernet"


class Comunication(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.EmailField()
    tekst = models.TextField(max_length=1000)

    class Meta:
        app_label = "main"
        db_table = "mesage"
