# Generated by Django 5.0.6 on 2024-08-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0008_cine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.TextField(null=True),
        ),
    ]
