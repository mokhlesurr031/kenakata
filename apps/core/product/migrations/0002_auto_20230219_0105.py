# Generated by Django 3.2 on 2023-02-19 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='offer_amount',
            new_name='offer_rate',
        ),
        migrations.AddField(
            model_name='product',
            name='price_excluding_offer',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_including_offer',
            field=models.FloatField(default=0.0),
        ),
    ]