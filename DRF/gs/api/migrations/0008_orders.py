# Generated by Django 5.1.7 on 2025-04-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_pre_time_menulistitem_pretime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('table_number', models.IntegerField()),
            ],
        ),
    ]
