# Generated by Django 4.1 on 2022-08-19 16:02

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
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('cover', models.FileField(blank=True, null=True, upload_to='vehicles')),
                ('is_available', models.BooleanField(blank=True, default=True, null=True)),
                ('map_link', models.CharField(blank=True, max_length=40, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('from_location', models.CharField(blank=True, max_length=40, null=True)),
                ('to_location', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('method', models.CharField(blank=True, max_length=20, null=True)),
                ('txn_id', models.CharField(blank=True, max_length=20, null=True)),
                ('account_no', models.CharField(blank=True, max_length=20, null=True)),
                ('request_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('passenger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ride_share.vehicle')),
            ],
        ),
    ]
