from django.db import models
# from datetime import datetime
# from asyncio.windows_events import NULL
# from operator import mod
# from datetime import *
from mainapp.models import UserdetailsModel



class DeviceModel(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_user = models.ForeignKey(UserdetailsModel, on_delete=models.CASCADE, related_name='device_user',null=True)
    device_node = models.CharField(verbose_name='Device_node', db_column="device-node", max_length=100, blank=False,null=True)
    device_type = models.CharField(verbose_name='Device_type', db_column="device-type", max_length=200, blank=False,null=False)
    device_name = models.CharField(verbose_name='Device_name', db_column="device-name", max_length=200, blank=False,null=False)
    device_ip = models.CharField(verbose_name='Device_ip', db_column="device-ip", max_length=200, blank=False,null=False)
    device_status = models.CharField(verbose_name='Device_status', db_column="device-status",default='pending', max_length=200, blank=False,null=True)
    device_server = models.CharField(default='Null',verbose_name='Device_server', db_column="device-server", max_length=100, blank=False,null=True)

    datetime_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='device_details'


class FileModel(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(verbose_name='File_name', db_column="file-name", max_length=1000, blank=False,null=False)
    file_size = models.IntegerField(verbose_name='File_size', db_column="file-size", blank=False,null=False)
    file_type = models.CharField(verbose_name='File_type', db_column="file-type", max_length=50, blank=False,null=True)

    file = models.FileField(verbose_name='file', db_column="file", upload_to='Mobile/user-data/', blank=False, null=True,)
    file_user = models.ForeignKey(UserdetailsModel, on_delete=models.CASCADE, related_name='file_user',null=True)
    file_node = models.CharField(verbose_name='File_node', db_column="file-node", max_length=100, blank=False,null=True)
    file_device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, related_name='file_device',null=True)
    # file_device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, related_name='file_device',null=True)
    
    # device_name = models.CharField(verbose_name='Device_name', db_column="device-name", max_length=200, blank=False,null=False)
    # device_ip = models.CharField(verbose_name='Device_ip', db_column="device-ip", max_length=200, blank=False,null=False)
    datetime_created = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='file_details'



















# class upload_data(models.Model):
#     d_id = models.AutoField(primary_key=True)
#     file_name = models.CharField(verbose_name='File_name', db_column="file-name", max_length=50, blank=False,null=False)
#     file_size = models.CharField(verbose_name='File_size', db_column="file-size", max_length=50, blank=False,null=False)
#     file_type = models.CharField(db_column='File_type', verbose_name='file_type', max_length=100, null=True, blank=True)
#     file = models.FileField(verbose_name='file', db_column="file", upload_to='Mobile/user-data/', blank=False, null=True,)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='upload_data'

# class lap_data(models.Model):
#     l_id = models.AutoField(primary_key=True)
#     file_name = models.CharField(verbose_name='File_name', db_column="file-name", max_length=50, blank=False,null=False)
#     file_size = models.CharField(verbose_name='File_size', db_column="file-size", max_length=50, blank=False,null=False)
#     file_type = models.CharField(db_column='File_type', verbose_name='file_type', max_length=100, null=True, blank=True)
#     file = models.FileField(verbose_name='file', db_column="file", upload_to='Mobile/user-data/', blank=False, null=True,)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='lap_data'

# class ip_data(models.Model):
#     d_id = models.AutoField(primary_key=True)
#     file_name = models.CharField(verbose_name='File_name', db_column="file-name", max_length=50, blank=False,null=False)
#     file_size = models.CharField(verbose_name='File_size', db_column="file-size", max_length=50, blank=False,null=False)
#     file_type = models.CharField(db_column='File_type', verbose_name='file_type', max_length=100, null=True, blank=True)
#     file = models.FileField(verbose_name='file', db_column="file", upload_to='Mobile/user-data/', blank=False, null=True,)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='ip_data'

# class tab_data(models.Model):
#     d_id = models.AutoField(primary_key=True)
#     file_name = models.CharField(verbose_name='File_name', db_column="file-name", max_length=50, blank=False,null=False)
#     file_size = models.CharField(verbose_name='File_size', db_column="file-size", max_length=50, blank=False,null=False)
#     file_type = models.CharField(db_column='File_type', verbose_name='file_type', max_length=100, null=True, blank=True)
#     file = models.FileField(verbose_name='file', db_column="file", upload_to='Mobile/user-data/', blank=False, null=True,)
#     datetime_created = models.DateTimeField(default=datetime.now)
#     class Meta:
#         db_table='tab_data'