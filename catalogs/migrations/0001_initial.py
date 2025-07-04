# Generated by Django 5.1.4 on 2025-06-24 09:51

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('key', models.CharField(choices=[('muscle', 'Musculo'), ('equipment', 'Equipo')], max_length=140)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.utils.custom_upload_to)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
