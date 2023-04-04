from django.urls import path, include
from rest_framework import routers
from tasklist.views import TasklistViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasklistViewSet)

urlpatterns = [
    path('', include(router.urls))
]