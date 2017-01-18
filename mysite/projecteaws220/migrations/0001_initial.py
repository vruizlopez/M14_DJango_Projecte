# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('apellido1', models.CharField(max_length=15)),
                ('apellido2', models.CharField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=15)),
                ('version', models.CharField(max_length=15)),
                ('motor', models.CharField(max_length=100)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precioTotal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('usuario', models.ForeignKey(to='projecteaws220.Usuario')),
                ('vehiculo', models.ForeignKey(to='projecteaws220.Vehiculo')),
            ],
        ),
    ]
