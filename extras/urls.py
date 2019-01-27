from django.urls import path, include
from .routers import router
from .views import SpringSrvApiView


urlpatterns = [
    path('spring/', include(router.urls)),
]