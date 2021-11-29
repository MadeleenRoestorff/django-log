# Generated by Django 3.2.8 on 2021-11-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20211125_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created_server', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated_server', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('make', models.CharField(blank=True, max_length=60, null=True)),
                ('model', models.CharField(blank=True, max_length=60, null=True)),
                ('registration', models.CharField(blank=True, max_length=60, null=True)),
                ('odometer_long', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='fuellog',
            old_name='odometer',
            new_name='odometer_short',
        ),
        migrations.AlterField(
            model_name='fuellog',
            name='station',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]