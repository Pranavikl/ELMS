# Generated by Django 5.0.1 on 2024-01-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('Branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('AgBSC', 'AgBSC')], max_length=20)),
                ('Year', models.CharField(choices=[('1st yr', '1st yr'), ('1st yr', '2nd yr'), ('3rd yr', '3rd yr'), ('4th yr', '4th yr')], max_length=20)),
            ],
        ),
    ]
