from rest_framework.generics import GenericAPIView
from . import mixins

class NonRestListAPIView(mixins.NonRestListModelMixin,
                  GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NonRestRetrieveAPIView(mixins.NonRestRetrieveModelMixin,
                  GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
