# Generated by Django 5.2.4 on 2025-07-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0002_desarrollador_remove_videojuego_plataforma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseña',
            name='puntaje',
            field=models.IntegerField(),
        ),
    ]
