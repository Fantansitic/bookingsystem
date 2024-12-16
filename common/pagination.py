import math
from collections import OrderedDict
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class CachingPaginator(Paginator):
    def __get_count(self):
        if not hasattr(self,'_count'):
            self._count = None
        return self.object_list.count()
    
    count = property(__get_count)

class PageNumberPaginationEx(PageNumberPagination):
    page_size_query_param = 'size'
    django_paginator_class = CachingPaginator

    def __get_count(self,queryset):
        return queryset.count()

    def paginate_queryset(self, queryset, request, view=None):
        self.total = self.__get_count(queryset)
        self.page_size = self.get_page_size(request)
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        return OrderedDict([
            ('total',self.total),
            ('size',len(self.page)),
            ('pages',math.ceil(self.total/self.page_size)),
            ('current',self.page.number),
            ('records',data)
        ])