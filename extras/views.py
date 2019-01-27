from zeep import Client
from zeep.helpers import serialize_object
from rest_framework import status
from rest_framework.response import Response
from utils.non_rest.generics import NonRestListAPIView, NonRestRetrieveAPIView
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


class SoapResponse(NonRestRetrieveAPIView):
    url = (
        'http://webservices.oorsprong.org/'
        'websamples.countryinfo/'
        'CountryInfoService.wso?WSDL'
    )
    method = 'FullCountryInfoAllCountries'
    
    def retrieve(self, request, *args, **kwargs):
        client = Client(self.url)
        service = client.service
        info_from_all_countries = getattr(service, self.method)()
        result = []
        for info in info_from_all_countries:
            result.append(serialize_object(info))
        out = {
            'status': status.HTTP_200_OK,
            'msj': None,
            'extra': result,
        }
        return Response(out)
