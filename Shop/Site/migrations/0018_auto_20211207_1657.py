# Generated by Django 2.2 on 2021-12-07 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0017_auto_20211207_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Site.Profile', verbose_name='Покупатель'),
            preserve_default=False,
        ),
    ]