from django.db import models
from datetime import datetime
from asyncio.windows_events import NULL
from operator import mod
# from datetime import *



class UserdetailsModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(verbose_name='Name', db_column="name", max_length=50, blank=False,null=False)
    user_email = models.EmailField(db_column='email', verbose_name='Email', max_length=100, null=True, blank=True)
    user_password=models.CharField(verbose_name='Password',db_column="password",max_length=100,blank=False,null=False)
    user_contact = models.BigIntegerField(verbose_name='contact', db_column="contact", blank=False,null=False)
    user_region = models.CharField(verbose_name='User_region', db_column="user_region", max_length=50, blank=False,null=False)
    user_photo = models.FileField(verbose_name='User_photo', db_column="image", upload_to='Mobile/user-image/', blank=False)
    datetime_created = models.DateTimeField(default=datetime.now)
    user_status=models.CharField(default='pending',max_length=50,null=True)
    user_server=models.CharField(default='none',max_length=200,null=True)

    class Meta:
        db_table='user_details'





















# class mobile_reg(models.Model):
#     m_id = models.AutoField(primary_key=True)
#     name = models.CharField(verbose_name='Name', db_column="name", max_length=50, blank=False,null=False)
#     phone = models.BigIntegerField(verbose_name='Phone', db_column="phone", blank=False,null=False)
#     email = models.EmailField(db_column='email', verbose_name='Email', max_length=100, null=True, blank=True)
#     pwd=models.CharField(verbose_name='Password',db_column="pwd",max_length=100,blank=False,null=False)
#     image = models.FileField(verbose_name='Image', db_column="image", upload_to='Mobile/user-image/', blank=False)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='mobile_reg'

# class lap_reg(models.Model):
#     l_id = models.AutoField(primary_key=True)
#     name = models.CharField(verbose_name='Name', db_column="name", max_length=50, blank=False,null=False)
#     phone = models.BigIntegerField(verbose_name='Phone', db_column="phone", blank=False,null=False)
#     city = models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,null=False)
#     email = models.EmailField(db_column='email', verbose_name='Email', max_length=100, null=True, blank=True)
#     pwd=models.CharField(verbose_name='Password',db_column="pwd",max_length=100,blank=False,null=False)
#     image = models.FileField(verbose_name='Image', db_column="image", upload_to='Mobile/user-image/', blank=False)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='lap_reg'

# class camera_reg(models.Model):
#     c_id = models.AutoField(primary_key=True)
#     name = models.CharField(verbose_name='Name', db_column="name", max_length=50, blank=False,null=False)
#     phone = models.BigIntegerField(verbose_name='Phone', db_column="phone", blank=False,null=False)
#     city = models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,null=False)
#     email = models.EmailField(db_column='email', verbose_name='Email', max_length=100, null=True, blank=True)
#     pwd=models.CharField(verbose_name='Password',db_column="pwd",max_length=100,blank=False,null=False)
#     image = models.FileField(verbose_name='Image', db_column="image", upload_to='Mobile/user-image/', blank=False)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='camera_reg'
    
# class tab_reg(models.Model):
#     t_id = models.AutoField(primary_key=True)
#     name = models.CharField(verbose_name='Name', db_column="name", max_length=50, blank=False,null=False)
#     phone = models.BigIntegerField(verbose_name='Phone', db_column="phone", blank=False,null=False)
#     city = models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,null=False)
#     email = models.EmailField(db_column='email', verbose_name='Email', max_length=100, null=True, blank=True)
#     pwd=models.CharField(verbose_name='Password',db_column="pwd",max_length=100,blank=False,null=False)
#     image = models.FileField(verbose_name='Image', db_column="image", upload_to='Mobile/user-image/', blank=False)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='tab_reg'