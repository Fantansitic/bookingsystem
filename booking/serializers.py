from booking import models
from rest_framework import serializers

class BookingFormSerializer(serializers.ModelSerializer):
    LoggeTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.BookingForm
        fields = '__all__'