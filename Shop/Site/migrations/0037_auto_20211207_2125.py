# Generated by Django 2.2 on 2021-12-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0036_auto_20211207_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
