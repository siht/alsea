from django.urls import path, include
from .routers import router
from .views import DiscographyListView


urlpatterns = [
    path('', include(router.urls)),
    path('discography', DiscographyListView.as_view()),
]