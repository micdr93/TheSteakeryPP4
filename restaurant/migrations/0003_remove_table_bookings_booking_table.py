# Generated by Django 4.2.16 on 2024-09-15 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking_specialrequest_table_delete_mymodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='bookings',
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.table'),
        ),
    ]
