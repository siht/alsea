from rest_framework.response import Response

class NonRestListMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        old_serializer = {
            'status': 200,
            'msj': serializer.data,
            'extra': ''
        }
        return Response(old_serializer)