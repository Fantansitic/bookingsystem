from django.db import models
from common.utils import UUIDTools
# Create your models here.

class KeyLogge(models.Model):
    BookFormId = models.CharField(verbose_name='BookFormId',db_column='BookFormId',
                                  max_length=50,editable=False)
    ServerRoomName = models.CharField(verbose_name='BookRoomName',db_column='BookRoomName',
                                      max_length=255,blank=False)
    ApplicantPeople = models.CharField(verbose_name='ApplicantPeople',db_column='ApplicantPeople',
                                       max_length=255)
    ApplicantConcat = models.CharField(verbose_name='ApplicantConcat',db_column='ApplicantConcat',
                                       max_length=11,blank=False)
    OperatePeople = models.CharField(verbose_name='OperatePeople',db_column='OperatePeople',
                                     max_length=255)
    OperateConcat = models.CharField(verbose_name='OperateConcat',db_column='OperateConcat',
                                     max_length=11,blank=False)
    RoomKey = models.CharField(verbose_name='RoomKey',db_column='RoomKey',
                               max_length=10,blank=False)
    OperateTime = models.DateTimeField(verbose_name='OperateTime',db_column='OperateTime')
    
    Id = models.CharField(verbose_name='PK',db_column='Id',max_length=50,editable=False,primary_key=True,default=UUIDTools.uuid4)
    
    class Meta:
        db_table = 'keylogge'
        verbose_name_plural = verbose_name = 'keylogge'