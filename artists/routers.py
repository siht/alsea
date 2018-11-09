from rest_framework import routers
from .views import ArtistViewSet


router = routers.DefaultRouter()
router.register('artists', ArtistViewSet)
