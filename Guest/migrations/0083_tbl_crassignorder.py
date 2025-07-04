# Generated by Django 5.0.2 on 2024-04-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0082_delete_tbl_crassignorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_crassignorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crassign_date', models.DateField(auto_now_add=True)),
                ('crassign_message', models.CharField(max_length=50)),
                ('crassign_status', models.IntegerField(default='0')),
                ('customisedrequests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_customisedrequests')),
                ('sp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_sp')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newuser')),
            ],
        ),
    ]
