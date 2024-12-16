from django.db import models
from common import constants as c
from common.utils import UUIDTools
# Create your models here.

class Account(models.Model):
    AccountId = models.CharField(verbose_name='PK',db_column='AccountId',
                                 max_length=50,editable=False,
                                 primary_key=True,default=UUIDTools.uuid4)
    WordId = models.CharField(verbose_name='WorkId',db_column='WorkId',
                              max_length=50,blank=True,null=True)
    Level = models.IntegerField(verbose_name='Level',db_column='Level',
                                blank=True,choices=c.Manager_Level_Choices,default=c.Manager_Level_Visitor)
    AccountNumber = models.CharField(verbose_name="AccountNumber",db_column='Account',
                                     max_length=25)
    Salt = models.CharField(verbose_name='Salt',db_column='Salt',max_length=10)
    PassWord = models.CharField(verbose_name='PassWord',db_column='PassWord',max_length=32)
    Mobile = models.CharField(verbose_name='Mobile',db_column='Mobile',max_length=11)
    Deleted = models.IntegerField(verbose_name='AccountStatus',db_column='IsDeleted',
                                  default=c.AccountAlive,choices=c.Account_Status_Choices)
    
    class Meta:
        verbose_name_plural = verbose_name = 'Acocunt'
        db_table = 'scydauthaccount'