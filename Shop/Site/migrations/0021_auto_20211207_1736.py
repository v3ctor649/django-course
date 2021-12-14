# Generated by Django 2.2 on 2021-12-07 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0020_auto_20211207_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Site.Clothes'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_in_order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.Clothes'),
        ),
        migrations.AlterField(
            model_name='profile_cart',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Site.Clothes'),
        ),
    ]
