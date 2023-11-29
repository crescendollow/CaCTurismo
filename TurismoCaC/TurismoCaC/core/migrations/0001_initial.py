# Generated by Django 4.2.7 on 2023-11-29 02:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('descripcion', models.CharField(max_length=1000, null=True, verbose_name='Descripcion del Hotel')),
                ('estrellas', models.IntegerField(verbose_name='Estrellas:')),
                ('desayuno', models.BooleanField(default=False, verbose_name='Desayuno:')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('username', models.CharField(max_length=15, verbose_name='Username')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre:')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio:')),
                ('fecha_salida', models.DateField(default='', verbose_name='Fecha de Salida:')),
                ('cantidad_personas', models.IntegerField(default=1, verbose_name='Cantidad de Personas:')),
                ('numero_reserva', models.IntegerField(default=893235)),
                ('fecha_reserva', models.DateField(default=django.utils.timezone.now)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hotel')),
                ('usuarios', models.ManyToManyField(to='core.usuario', verbose_name='Usuario:')),
            ],
        ),
    ]
