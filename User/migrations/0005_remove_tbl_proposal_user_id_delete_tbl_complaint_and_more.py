# Generated by Django 5.0.2 on 2024-03-25 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_tbl_proposal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_proposal',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
        migrations.DeleteModel(
            name='tbl_proposal',
        ),
    ]
