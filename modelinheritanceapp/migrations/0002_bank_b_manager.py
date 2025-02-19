# Generated by Django 5.1.5 on 2025-02-19 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritanceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('b_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='b_manager',
            fields=[
                ('bank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelinheritanceapp.bank')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
            bases=('modelinheritanceapp.bank',),
        ),
    ]
