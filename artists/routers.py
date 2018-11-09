from rest_framework import routers
from .views import (
	ArtistViewSet,
	AlbumViewSet,
)


router = routers.DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('artists', ArtistViewSet)
