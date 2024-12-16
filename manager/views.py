import datetime
from manager import services
from rest_framework import status  
from common import constants as c
from django.shortcuts import render
from booking import models as Bmodel
from common.viewsets import BaseViewSet
from booking import models as bookmodel
from common.response import JsonResponse
from rest_framework.decorators import action
from manager import permissions,authentications,serializers,forms,models

# Create your views here.

class BooklistViewSet(BaseViewSet):
    permission_classes = (permissions.LoginRequire,)
    serializer_class = serializers.WaitFromSerializer
    authentication_classes = (authentications.TokenAuthentication,)
    queryset = bookmodel.BookingForm.objects.filter().order_by('-LoggeTime')

    def get_queryset(self):
        return self.queryset.filter(FormStatus=c.Form_Status_Wait)

    @action(methods=['GET'],detail=False)
    def waitting(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset=queryset)    
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)    
            return JsonResponse(code=c.API_MESSAGE_OK,message='ok',data=serializer.data)

    @action(methods=['POST'],detail=False)
    def setroomkey(self,request):
        form = forms.KeyForms(request.data)
        if not form.is_valid():
            return JsonResponse(message=form.errors,code=status.HTTP_400_BAD_REQUEST,
                    status=status.HTTP_400_BAD_REQUEST)
        data = form.cleaned_data
        m = Bmodel.BookingForm.objects.filter(FormId=data['BookFormId'],FormStatus=c.Form_Status_Wait).first()
        if m is None:
            return JsonResponse(code=c.API_MESSAGE_NOT_FOUND,message='资源已结束,请刷新后查看',status=status.HTTP_404_NOT_FOUND)
        
        if data['Key'] == "-1":
            m.FormStatus=c.Form_Status_Reject
            m.save()
            return JsonResponse(code=c.API_MESSAGE_OK,message='reject')
        
        models.KeyLogge.objects.create(
            BookFormId = m.FormId,
            ServerRoomName = m.ServerRoomName,
            ApplicantPeople = m.ApplicantName,
            ApplicantConcat = m.Mobile,
            RoomKey = data['Key'],
            OperatePeople = 'Admin',
            OperateTime = datetime.datetime.now(),  
            OperateConcat = request.user,
        )
        m.FormStatus = c.Form_Status_Accept
        m.save()
        if m.Email:
                services.send_key_by_email(m.Email,data['Key'])
        return JsonResponse(code=c.API_MESSAGE_OK,message='ok')
    

class HistoryListViewSet(BaseViewSet):

    permission_classes = (permissions.LoginRequire,)
    serializer_class = serializers.HistorySerializer
    authentication_classes = (authentications.TokenAuthentication,)
    queryset = models.KeyLogge.objects.filter().order_by('-OperateTime')
    search_fields = ('ApplicantConcat',)

    @action(methods=['GET'],detail=False)
    def history(self,request):
        start_time = self.request.GET.get('startime','')
        end_time = self.request.GET.get('endtime','')
        if not start_time:
            queryset = self.filter_queryset(self.queryset)
        else:
            start_time = datetime.datetime.strptime(start_time, "%Y%m%d")
            if not end_time:
                queryset = self.filter_queryset(self.queryset.filter(OperateTime__gte=start_time))
            else:
                end_time = datetime.datetime.strptime(end_time, "%Y%m%d")
                queryset = self.filter_queryset(self.queryset.filter(OperateTime__range=(start_time,end_time)))
        page = self.paginate_queryset(queryset=queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True) 
            return JsonResponse(code=c.API_MESSAGE_OK,message='ok',data=serializer.data)
