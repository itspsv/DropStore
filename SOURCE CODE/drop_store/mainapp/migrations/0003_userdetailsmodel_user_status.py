# Generated by Django 4.1.2 on 2022-11-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_userdetailsmodel_delete_camera_reg_delete_lap_reg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetailsmodel',
            name='user_status',
            field=models.CharField(default='pending', max_length=50, null=True),
        ),
    ]
