# Generated by Django 5.1.6 on 2025-04-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='College',
            new_name='college',
        ),
    ]
