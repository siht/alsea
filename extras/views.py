from rest_framework.response import Response
from utils.non_rest.generics import NonRestListAPIView
from utils.non_rest.viewsets import NonRestModelViewSet
from .models import SpringService
from .serializers import SpringSrvSerializer

class SpringSrvApiView(NonRestModelViewSet):
    http_methods = ['list', 'get']
    queryset = SpringService.objects.all()
    serializer_class = SpringSrvSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.serializer_class.Meta.model()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
