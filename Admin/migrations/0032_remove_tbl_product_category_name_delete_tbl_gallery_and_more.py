# Generated by Django 5.0.2 on 2024-03-05 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_tbl_product_tbl_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_product',
            name='category_name',
        ),
        migrations.DeleteModel(
            name='tbl_gallery',
        ),
        migrations.DeleteModel(
            name='tbl_product',
        ),
    ]
