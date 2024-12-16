from account import models
from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    class Meta:
        models = models.Account
        fields = ('AccountId','Level','AccountNumber','Mobile','Deleted')