import datetime
from rest_framework import status 
from common import constants as c
from django.shortcuts import render
from common.viewsets import BaseViewSet
from common.response import JsonResponse
from rest_framework.decorators import action
from booking import forms,models,serializers,services
# Create your views here.

class BookingFormViewSet(BaseViewSet):

    serializer_class = serializers.BookingFormSerializer
    queryset = models.BookingForm.objects.filter()

    @action(methods=['POST'],detail=False)
    def bookserverroom(self,request):
        form = forms.BookForms(request.data)
        if not form.is_valid():
            return JsonResponse(message=form.errors,code=status.HTTP_400_BAD_REQUEST,
                                status=status.HTTP_400_BAD_REQUEST)
        data = form.cleaned_data
        if not services.check_real_phone(data['Mobile']):
            return JsonResponse(message='pleace enter a real phone number',
                                status=status.HTTP_400_BAD_REQUEST,
                                code=status.HTTP_400_BAD_REQUEST)
        models.BookingForm.objects.create(
            ServerRoomName = data['ServerRoomName'],
            ApplicantName = data['ApplicantName'],
            Mobile = data['Mobile'],
            LoggeTime = datetime.datetime.now(),
            FormStatus = c.Form_Status_Wait,
            Email = data['Email']
        )
        return JsonResponse(code=c.API_MESSAGE_OK,message='Submission Successful',
                            status=status.HTTP_201_CREATED)