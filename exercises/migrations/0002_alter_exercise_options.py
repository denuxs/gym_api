# Generated by Django 5.1.4 on 2025-03-03 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['muscle']},
        ),
    ]
