from django.conf.urls import url, include
from . import views, serializers
from .views import BoxViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'add', BoxViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),

]
