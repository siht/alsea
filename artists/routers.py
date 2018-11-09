from rest_framework import routers
from .serializers import ArtistViewSet


router = routers.DefaultRouter()
router.register('artists', ArtistViewSet)
