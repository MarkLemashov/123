# Generated by Django 2.2.15 on 2020-10-25 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20201025_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
        migrations.AddField(
            model_name='customer',
            name='cars',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
