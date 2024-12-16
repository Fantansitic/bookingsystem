from rest_framework import status
from django.shortcuts import render
from common import constants as c
from common.viewsets import BaseViewSet
from common.response import JsonResponse
from rest_framework.decorators import action
from account import serializers,models,forms,services
# Create your views here.

class AccountViewSet(BaseViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.filter()

    @action(detail=False, methods=['POST'])
    def login(self,request):
        form = forms.LoginForm(request.data)
        if not form.is_valid():
            return JsonResponse(message=form.errors,code=status.HTTP_400_BAD_REQUEST,status=status.HTTP_400_BAD_REQUEST)
        data = form.cleaned_data
        flag,message = services.login(account=data["Account"],password=data["PassWord"])
        if not flag:
            return JsonResponse(message=message,code=status.HTTP_400_BAD_REQUEST,status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(data=message,code=c.API_MESSAGE_OK,message='ok')