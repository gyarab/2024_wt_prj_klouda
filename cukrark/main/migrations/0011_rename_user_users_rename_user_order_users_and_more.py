# Generated by Django 5.1.6 on 2025-04-01 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='users',
        ),
    ]
