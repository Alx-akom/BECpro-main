# Generated by Django 4.2.3 on 2023-08-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_remove_member_days_member_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
