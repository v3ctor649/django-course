# Generated by Django 2.2 on 2021-12-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0041_orders_data_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='data_field',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
