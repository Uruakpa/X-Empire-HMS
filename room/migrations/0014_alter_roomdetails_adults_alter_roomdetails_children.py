# Generated by Django 5.0.3 on 2024-09-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_rooms_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetails',
            name='adults',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
