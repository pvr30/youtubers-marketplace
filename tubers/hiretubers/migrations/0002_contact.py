# Generated by Django 3.2.8 on 2021-10-16 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]