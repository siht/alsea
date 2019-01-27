from django.urls import path, include
from .routers import router
from .views import SoapResponse


urlpatterns = [
    path('spring/', include(router.urls)),
    path('soap/', SoapResponse.as_view()),
]