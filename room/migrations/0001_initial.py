# Generated by Django 5.0.3 on 2024-09-12 15:04

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
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('Home', 'Home'), ('Personal', 'Personal'), ('Official', 'Official'), ('Business', 'Business')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('zipcode', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IdentityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('NIN', 'NIN'), ('PASSPORT', 'PASSPORT'), ("VOTER'S CARD", "VOTER'S CARD"), ("DRIVER'S LICENSE", "DRIVER'S LICENSE")], max_length=60)),
                ('id_number', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Cash payment', 'Cash payment'), ('Card Payment', 'Card Payment'), ('Bank Transfer', 'Bank Transfer')], max_length=100)),
                ('amount', models.FloatField()),
                ('payment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.SmallIntegerField()),
                ('numberOfBeds', models.SmallIntegerField()),
                ('roomType', models.CharField(choices=[('King', 'King'), ('Luxury', 'Luxury'), ('Normal', 'Normal'), ('Economic', 'Economic')], max_length=20)),
                ('price', models.FloatField()),
                ('statusStartDate', models.DateField(null=True)),
                ('statusEndDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('roomPrice', models.FloatField()),
                ('status', models.CharField(blank=True, choices=[('Available', 'Available'), ('Booked', 'Booked')], max_length=50, null=True)),
                ('checkout', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/roomimages')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfReservation', models.DateField(default=django.utils.timezone.now)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.guest')),
                ('roomNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
        migrations.CreateModel(
            name='Dependees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
            ],
        ),
        migrations.CreateModel(
            name='GuestDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Dr', 'Dr')], max_length=15)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('occupation', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_det', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.contactdetails')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('payments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.guest')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adults', models.IntegerField(blank=True, null=True)),
                ('children', models.IntegerField(blank=True, null=True)),
                ('roomNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.rooms')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('arrival_from', models.CharField(max_length=255)),
                ('reservation_date', models.DateField(auto_now=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.guestdetails')),
                ('payment_det', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.payment')),
                ('room_det', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.roomdetails')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.rooms')),
            ],
            options={
                'ordering': ['-reservation_date', '-date_edited'],
            },
        ),
        migrations.CreateModel(
            name='RoomServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(default=django.utils.timezone.now)),
                ('servicesType', models.CharField(choices=[('Food', 'Food'), ('Cleaning', 'Cleaning'), ('Technical', 'Technical')], max_length=20)),
                ('price', models.FloatField()),
                ('curBooking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
        migrations.AddField(
            model_name='rooms',
            name='roomType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.roomtype'),
        ),
    ]
