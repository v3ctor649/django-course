# Generated by Django 2.2 on 2021-12-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0011_auto_20211205_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='time',
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]