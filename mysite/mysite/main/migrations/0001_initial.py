# Generated by Django 2.2.6 on 2019-11-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('tekst', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=150)),
                ('nazwisko', models.CharField(max_length=200)),
                ('zdj', models.ImageField(height_field=600, upload_to='', width_field=600)),
                ('git_hub', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('kolejnosc', models.IntegerField(default=98)),
            ],
        ),
    ]