# Generated by Django 5.0.2 on 2024-04-04 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0051_tbl_packageinterest_tbl_assignorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_packageinterest',
            name='package',
        ),
        migrations.RemoveField(
            model_name='tbl_packageinterest',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_assignorder',
        ),
        migrations.DeleteModel(
            name='tbl_packageinterest',
        ),
    ]
