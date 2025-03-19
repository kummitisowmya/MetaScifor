from django.urls import path,include
from apiapp.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'api',StudentViewset)

urlpatterns=[path('',include(router.urls))]