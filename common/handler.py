import logging
from django.db import DatabaseError
from django.http import Http404
from rest_framework.views import exception_handler
from rest_framework.utils import serializer_helpers

from common.response import JsonResponse
from common import exceptions

logger = logging.getLogger('django')


def custom_exception_handler(exc, context):
    # Call REST framework's default exceptions handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    logger.debug('custom_exception_handler')
    logger.debug(response)
    if isinstance(exc, DatabaseError):
        logger.debug(exc)
        return JsonResponse(code=500, message='数据库异常请联系管理员', data=str(exc), status=500)
    if isinstance(exc, Http404):
        return JsonResponse(code=404, message='未找到您查询的数据', data=str(exc), status=404)
    if response is not None:
        if exc.detail:
            message = exc.detail
        else:
            message = exc.default_detail
        if isinstance(exc, exceptions.LogicalError):
            logger.debug(message)
            return JsonResponse(code=exc.code,
                                message='{} {}'.format(exc.code, message),
                                data=exc.data,
                                status=response.status_code)
        if isinstance(exc.detail, exceptions.exceptions.ErrorDetail):
            print(message)
            logger.debug(message)
            return JsonResponse(code=response.status_code,
                                message='{} {}'.format(response.status_code, message),
                                data=None,
                                status=response.status_code)
        if isinstance(exc.detail, serializer_helpers.ReturnDict):
            print(exc.default_detail)
            logger.debug(exc.default_detail)
            print(exc.detail)
            logger.debug(exc.detail)
            return JsonResponse(code=response.status_code,
                                message='{} {}'.format(response.status_code, exc.default_detail),
                                data=exc.detail,
                                status=response.status_code)
    print(exc)
    logger.debug(exc)
    return JsonResponse(code=500, message='未知错误请联系管理员', data=str(exc), status=500)
