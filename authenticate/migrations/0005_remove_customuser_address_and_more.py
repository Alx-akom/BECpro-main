# Generated by Django 4.2.3 on 2023-08-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_customuser_date_of_birth_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]