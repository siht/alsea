from rest_framework.viewsets import GenericViewSet
from . import mixins

class NonRestModelViewSet(mixins.NonRestCreateModelMixin,
                   mixins.NonRestRetrieveModelMixin,
                   mixins.NonRestUpdateModelMixin,
                   mixins.NonRestDestroyModelMixin,
                   mixins.NonRestListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass