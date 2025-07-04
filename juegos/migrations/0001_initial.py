# Generated by Django 5.2.3 on 2025-07-03 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=50)),
                ('fecha_salida', models.DateField()),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=3)),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.videojuego')),
            ],
        ),
    ]
