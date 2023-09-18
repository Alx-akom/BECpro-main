# Generated by Django 4.2.3 on 2023-08-16 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('days', models.CharField(choices=[('Sunday', 'Sunday')], max_length=200, null=True)),
                ('time_slot', models.CharField(choices=[('8-10 am', '8-10 am'), ('4-6 pm', '4-6 pm')], max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('days', models.CharField(choices=[('Wednesday', 'Wednesday')], max_length=200, null=True)),
                ('time_slot', models.CharField(choices=[('8-10 am', '8-10 am'), ('4-6 pm', '4-6 pm')], max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('days', models.CharField(choices=[('Saturday', 'Saturday')], max_length=200, null=True)),
                ('time_slot', models.CharField(choices=[('8-10 am', '8-10 am'), ('4-6 pm', '4-6 pm')], max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(choices=[('Family Riding Monthly', 'Family Riding Monthly'), ('Family Riding Yearly', 'Family Riding Yearly'), ('Family Polo Monthly', 'Family Polo Monthly'), ('Family Polo Yearly', 'Family Polo Yearly'), ('Single Riding Monthly', 'Single Riding Monthly'), ('Single Riding Yearly', 'Single Riding Yearly'), ('Single Polo Monthly', 'Single Polo Monthly'), ('Single Polo Yearly', 'Single Polo Yearly')], max_length=150)),
                ('price', models.IntegerField(null=True)),
                ('activity', models.CharField(choices=[('Riding', 'Riding'), ('Polo', 'Polo')], max_length=150, null=True)),
                ('duration', models.CharField(choices=[(' Monthly', ' Monthly'), (' Yearly', ' Yearly')], max_length=150, null=True)),
                ('duration_in_months', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('username', models.CharField(max_length=150, null=True, unique=True)),
                ('phone', models.CharField(max_length=150, null=True)),
                ('age', models.IntegerField(default=18)),
                ('address', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('postal_code', models.CharField(max_length=150, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paystack_charge_id', models.CharField(blank=True, max_length=100)),
                ('paystack_access_code', models.CharField(blank=True, max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('activity', models.CharField(blank=True, max_length=100)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('date_paid', models.DateTimeField(null=True)),
                ('expiry_date', models.DateTimeField(null=True)),
                ('payment_for', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.membership')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForgetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
