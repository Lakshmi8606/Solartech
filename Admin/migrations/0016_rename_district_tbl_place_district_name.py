# Generated by Django 5.0.2 on 2024-02-20 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_tbl_syllabus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_place',
            old_name='district',
            new_name='district_name',
        ),
    ]
