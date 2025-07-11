# Generated by Django 5.0.2 on 2024-03-25 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_tbl_sp'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_name', models.CharField(max_length=500)),
                ('complaint_content', models.CharField(max_length=500)),
                ('complaint_postdate', models.DateField(auto_now_add=True)),
                ('complaint_reply', models.CharField(max_length=500)),
                ('complaint_replydate', models.DateField(null=True)),
                ('complaint_status', models.IntegerField(default='0')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newuser')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_desc', models.CharField(max_length=50)),
                ('proposal_date', models.CharField(max_length=50)),
                ('proposal_status', models.IntegerField(default='0')),
                ('electricity_usage', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newuser')),
            ],
        ),
    ]
