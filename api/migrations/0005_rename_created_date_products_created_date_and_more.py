# Generated by Django 4.2 on 2025-03-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_products_update_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Created_Date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='Update_Date',
            new_name='updated_date',
        ),
    ]
