# Generated by Django 4.2.5 on 2023-10-26 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='usuarios',
            field=models.ManyToManyField(through='core.Reserva', to='core.usuario'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuarios',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
