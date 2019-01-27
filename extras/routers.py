from rest_framework import routers	
from .views import SpringSrvApiView

router = routers.DefaultRouter()
router.register('spring-query', SpringSrvApiView)