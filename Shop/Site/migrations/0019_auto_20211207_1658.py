# Generated by Django 2.2 on 2021-12-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0018_auto_20211207_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.Profile', unique=True),
        ),
    ]
