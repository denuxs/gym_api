# Generated by Django 5.1.4 on 2025-04-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
