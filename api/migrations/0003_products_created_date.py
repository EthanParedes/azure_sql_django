# Generated by Django 4.2 on 2025-03-08 00:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Created_Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
