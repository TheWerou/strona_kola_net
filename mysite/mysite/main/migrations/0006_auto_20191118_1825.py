# Generated by Django 2.2.6 on 2019-11-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comunication_temat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunication',
            name='temat',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
