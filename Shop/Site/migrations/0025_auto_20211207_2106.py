# Generated by Django 2.2 on 2021-12-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0024_auto_20211207_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='Site.Clothes'),
        ),
    ]
