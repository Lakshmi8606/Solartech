# Generated by Django 5.0.2 on 2024-03-24 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0041_remove_tbl_product_brand_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=50)),
                ('product_image', models.FileField(upload_to='Assets/UserImage/')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_brand')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
                ('productcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.CharField(max_length=50)),
                ('product_photo', models.FileField(upload_to='Assets/productphoto/')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcategory')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_product')),
            ],
        ),
    ]
