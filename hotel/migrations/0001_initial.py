# Generated by Django 5.0.3 on 2024-09-10 17:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(choices=[('Movie', 'Movie'), ('Theater', 'Theater'), ('Conference', 'Conference'), ('Concert', 'Concert'), ('Entertainment', 'Entertainment'), ('Live Music', 'Live Music')], max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('menuItems', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('itemType', models.CharField(choices=[('Kitchen', 'kitchen'), ('Cleaning', 'cleaning'), ('Electronic', 'Electronic'), ('Textile ', 'textile '), ('Other', 'other')], max_length=20)),
                ('quantitiy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAmount', models.FloatField()),
                ('summary', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.guest')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfDependees', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.event')),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.guest')),
            ],
        ),
    ]
