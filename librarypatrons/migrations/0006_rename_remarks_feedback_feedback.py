# Generated by Django 5.0.1 on 2024-04-26 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarypatrons', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='remarks',
            new_name='feedback',
        ),
    ]