# Generated by Django 4.2.3 on 2023-08-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_rename_day3_days_rename_day3_member_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='days',
        ),
        migrations.AddField(
            model_name='member',
            name='days',
            field=models.ManyToManyField(to='members.days'),
        ),
    ]
