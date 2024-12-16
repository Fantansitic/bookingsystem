from manager import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register('wait',views.BooklistViewSet)
router.register('history',views.HistoryListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]