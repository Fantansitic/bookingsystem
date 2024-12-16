from django.db import models
from common.utils import UUIDTools
from common import constants as c
# Create your models here.

class BookingForm(models.Model):
    FormId = models.CharField(verbose_name='PK',db_column='FormId',
                              max_length=50,editable=False,
                              primary_key=True,default=UUIDTools.uuid4)
    ServerRoomId = models.CharField(verbose_name='RoomId',db_column='ServerRoomId',
                                    blank=True,null=True,max_length=25)
    ServerRoomName = models.CharField(verbose_name='RoomName',db_column='ServerRoomName',
                                      blank=True,max_length=255)
    ApplicantName = models.CharField(verbose_name='PeopleName',db_column='ApplicantName',
                                     max_length=255)
    Mobile = models.CharField(verbose_name='PhoneNumber',db_column='Mobile',
                              max_length=11)
    LoggeTime = models.DateTimeField(verbose_name='LoggeTime',db_column='LoggeTime')
    FormStatus = models.IntegerField(verbose_name='FormStatus',db_column='FormStatus',
                                     choices=c.Form_Status_Choices,blank=True)
    Email = models.CharField(verbose_name='Email',db_column='Email',
                             null=True,max_length=30)
    
    class Meta:
        db_table = 'bookform'
        verbose_name_plural = verbose_name = 'bookform'