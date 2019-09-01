from django.urls import path, include
from rest_framework import routers
from .views import index, dumpSchema, DbPropsAPI

router = routers.DefaultRouter()
router.register("api/babayaga", DbPropsAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('api/dump-schema', dumpSchema, name="dumpSchema"),
]
