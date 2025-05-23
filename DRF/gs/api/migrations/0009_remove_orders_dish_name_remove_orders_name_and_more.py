# Generated by Django 5.1.7 on 2025-04-04 18:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='dish_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='ordered_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('preparing', 'Preparing'), ('on_way', 'On the Way'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]
