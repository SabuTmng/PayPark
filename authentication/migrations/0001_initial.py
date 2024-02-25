# Generated by Django 3.1.3 on 2024-02-25 02:36

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('DateOfBirth', models.DateField(blank=True, default='2000-01-01', null=True)),
                ('CITIZENSHIP_NO', models.CharField(max_length=13, null=True)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_No', models.CharField(max_length=11, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Bill_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Generated_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Due_Date', models.DateTimeField(default=datetime.datetime(2024, 3, 24, 2, 36, 31, 936318, tzinfo=utc))),
                ('Paid_Status', models.BooleanField(default=False)),
                ('Bill_Amount', models.CharField(max_length=10)),
                ('Bill_Type', models.CharField(choices=[('MC', 'MemberRegistration'), ('VR', 'VehicleRegistration'), ('PV', 'ParkVehicle'), ('MR', 'MembershipRenewal')], default='MemberRegistration', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Employee_Type', models.CharField(choices=[('PE', 'ParkingEmployee'), ('PA', 'ParkingAdmin')], default='ParkingEmployee', max_length=2)),
                ('Account_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Member_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Account_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('Slot_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Occupied_Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('Vehicle_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Vehicle_Model', models.CharField(max_length=50)),
                ('Registeration_Date', models.DateTimeField(default=datetime.datetime(2024, 2, 25, 2, 36, 31, 938315, tzinfo=utc))),
                ('Approved_By', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.employee')),
                ('Member_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Payment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Payment_Date', models.DateTimeField(default=datetime.datetime(2024, 2, 25, 2, 36, 31, 937316, tzinfo=utc))),
                ('Payment_Method', models.CharField(choices=[('V', 'Visa'), ('M', 'Mastercard'), ('C', 'Cash')], default='Cash', max_length=2)),
                ('Bill_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.bill')),
                ('Payment_Supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('Parking_ID', models.AutoField(primary_key=True, serialize=False)),
                ('In_Time', models.DateTimeField(default=datetime.datetime(2024, 2, 25, 2, 36, 31, 939317, tzinfo=utc))),
                ('Out_Time', models.DateTimeField(blank=True, null=True)),
                ('Approved_By', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.employee')),
                ('Slot_Given', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.slot')),
                ('Vehicle_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('Membership_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Valid_From', models.DateTimeField(default=django.utils.timezone.now)),
                ('Valid_To', models.DateTimeField(default=datetime.datetime(2025, 2, 24, 2, 36, 31, 935317, tzinfo=utc))),
                ('Approved_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.employee')),
                ('Member_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='Membership_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.membership'),
        ),
    ]