# Generated by Django 5.1.4 on 2025-02-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('photo', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
