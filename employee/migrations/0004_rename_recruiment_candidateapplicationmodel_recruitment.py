# Generated by Django 5.1.6 on 2025-03-28 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidateapplicationmodel',
            old_name='recruiment',
            new_name='recruitment',
        ),
    ]
