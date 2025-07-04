# Generated by Django 5.0.2 on 2024-03-25 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0046_tbl_batterybrand_tbl_inverterbrand_tbl_panelbrand_and_more'),
        ('Guest', '0012_delete_tbl_proposal'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='tbl_quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_power', models.CharField(max_length=50)),
                ('acc_rate', models.CharField(max_length=50)),
                ('quotation_total', models.CharField(max_length=50)),
                ('quotation_status', models.IntegerField(default='0')),
                ('quotation_date', models.DateField(auto_now_add=True)),
                ('battery_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_batterybrand')),
                ('inverter_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_inverterbrand')),
                ('panel_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_panelbrand')),
                ('proposal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_proposal')),
            ],
        ),
    ]
