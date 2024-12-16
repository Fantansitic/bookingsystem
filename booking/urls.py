from booking import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register('', views.BookingFormViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]