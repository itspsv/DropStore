# Generated by Django 3.2.8 on 2022-09-19 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camera_reg',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('phone', models.BigIntegerField(db_column='phone', verbose_name='Phone')),
                ('city', models.CharField(db_column='city', max_length=50, verbose_name='City')),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Email')),
                ('pwd', models.CharField(db_column='pwd', max_length=100, verbose_name='Password')),
                ('image', models.FileField(db_column='image', upload_to='Mobile/user-image/', verbose_name='Image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'camera_reg',
            },
        ),
        migrations.CreateModel(
            name='lap_reg',
            fields=[
                ('l_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('phone', models.BigIntegerField(db_column='phone', verbose_name='Phone')),
                ('city', models.CharField(db_column='city', max_length=50, verbose_name='City')),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Email')),
                ('pwd', models.CharField(db_column='pwd', max_length=100, verbose_name='Password')),
                ('image', models.FileField(db_column='image', upload_to='Mobile/user-image/', verbose_name='Image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'lap_reg',
            },
        ),
        migrations.CreateModel(
            name='mobile_reg',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('phone', models.BigIntegerField(db_column='phone', verbose_name='Phone')),
                ('city', models.CharField(db_column='city', max_length=50, verbose_name='City')),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Email')),
                ('pwd', models.CharField(db_column='pwd', max_length=100, verbose_name='Password')),
                ('image', models.FileField(db_column='image', upload_to='Mobile/user-image/', verbose_name='Image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'mobile_reg',
            },
        ),
        migrations.CreateModel(
            name='tab_reg',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('phone', models.BigIntegerField(db_column='phone', verbose_name='Phone')),
                ('city', models.CharField(db_column='city', max_length=50, verbose_name='City')),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Email')),
                ('pwd', models.CharField(db_column='pwd', max_length=100, verbose_name='Password')),
                ('image', models.FileField(db_column='image', upload_to='Mobile/user-image/', verbose_name='Image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'tab_reg',
            },
        ),
    ]
