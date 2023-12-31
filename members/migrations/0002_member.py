# Generated by Django 4.2.3 on 2023-08-16 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=150, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('suspend', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=150, null=True)),
                ('guardian_name', models.CharField(max_length=150, null=True)),
                ('guardian_age', models.IntegerField(null=True)),
                ('guardian_weight', models.IntegerField(null=True)),
                ('guardian_height', models.IntegerField(null=True)),
                ('member1_full_name', models.CharField(max_length=150, null=True)),
                ('member1_age', models.IntegerField(null=True)),
                ('member1_email', models.CharField(max_length=150, null=True)),
                ('member1_weight', models.IntegerField(null=True)),
                ('member1_height', models.IntegerField(null=True)),
                ('member1_address', models.CharField(max_length=150, null=True)),
                ('member1_city', models.CharField(max_length=150, null=True)),
                ('member2_full_name', models.CharField(max_length=150, null=True)),
                ('member2_age', models.IntegerField(null=True)),
                ('member2_email', models.CharField(max_length=150, null=True)),
                ('member2_weight', models.IntegerField(null=True)),
                ('member2_height', models.IntegerField(null=True)),
                ('member2_address', models.CharField(max_length=150, null=True)),
                ('member2_city', models.CharField(max_length=150, null=True)),
                ('date_paid', models.DateField(null=True)),
                ('paid_until', models.DateField(null=True)),
                ('day1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.day1')),
                ('day2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.day2')),
                ('day3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.day3')),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.membership')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
