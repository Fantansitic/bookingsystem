from manager import models
from booking import models as B
from rest_framework import serializers

class WaitFromSerializer(serializers.ModelSerializer):
    LoggeTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = B.BookingForm
        fields = ('ServerRoomName','ApplicantName','LoggeTime','Mobile','FormId')


class HistorySerializer(serializers.ModelSerializer):
    OperateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.KeyLogge
        fields = ('ServerRoomName','ApplicantPeople','ApplicantConcat','OperatePeople','RoomKey','OperateTime')