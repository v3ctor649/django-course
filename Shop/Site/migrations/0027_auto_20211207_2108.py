# Generated by Django 2.2 on 2021-12-07 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0026_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Site.Clothes'),
            preserve_default=False,
        ),
    ]
