# Generated by Django 2.2 on 2021-12-07 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0033_auto_20211207_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('id', 'item')},
        ),
    ]
