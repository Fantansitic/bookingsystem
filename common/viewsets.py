from rest_framework import mixins
from common.response import JsonResponse
from rest_framework.viewsets import GenericViewSet
from common.pagination import PageNumberPaginationEx

class BaseViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,GenericViewSet):
        page_size_query_param = 'size'
        pagination_class = PageNumberPaginationEx

        def get_paginated_response(self, data):
            return JsonResponse(code=200, message='ok', data=super().get_paginated_response(data))