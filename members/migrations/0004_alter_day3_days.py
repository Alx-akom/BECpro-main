# Generated by Django 4.2.3 on 2023-08-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day3',
            name='days',
            field=models.CharField(choices=[('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Wednesday', 'Wednesday'), ('Friday', 'Friday')], max_length=200, null=True),
        ),
    ]
