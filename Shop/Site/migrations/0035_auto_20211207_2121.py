# Generated by Django 2.2 on 2021-12-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0034_auto_20211207_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
