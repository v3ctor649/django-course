# Generated by Django 2.2 on 2021-12-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0042_auto_20211211_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
