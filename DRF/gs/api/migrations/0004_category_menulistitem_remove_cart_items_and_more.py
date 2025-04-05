# Generated by Django 5.1.7 on 2025-04-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_foodcategory_menuitem_delete_fooditem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('likes', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
                ('views', models.PositiveIntegerField()),
                ('image', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serving_size', models.CharField(max_length=255)),
                ('prep_time', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('ingredients', models.JSONField()),
                ('nutrition', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_piece', models.PositiveIntegerField()),
                ('likes', models.PositiveIntegerField()),
                ('views', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
                ('pre_time', models.CharField(max_length=50)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('ingredients', models.JSONField()),
                ('nutrients', models.JSONField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('image', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.DeleteModel(
            name='FoodCategory',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
