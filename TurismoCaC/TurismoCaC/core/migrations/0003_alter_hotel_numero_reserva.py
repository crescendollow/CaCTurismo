# Generated by Django 4.2.6 on 2023-10-31 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hotel_desayuno_hotel_fecha_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='numero_reserva',
            field=models.IntegerField(default=634634),
        ),
    ]
