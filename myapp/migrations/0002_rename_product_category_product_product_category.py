# Generated by Django 4.2.3 on 2023-07-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_category',
            new_name='product_category',
        ),
    ]