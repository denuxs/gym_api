# Generated by Django 5.1.4 on 2025-05-22 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('measures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='user',
        ),
        migrations.AddField(
            model_name='measure',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.client'),
        ),
    ]
