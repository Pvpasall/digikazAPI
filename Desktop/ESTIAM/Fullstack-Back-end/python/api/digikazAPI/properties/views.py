from rest_framework import viewsets   
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
#from .permissions import IsGetRequest
#from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi


from .serializers import PropertiesSerializer
from .models import PropertiesModel


class PropertiesViewSet(viewsets.ModelViewSet):

    queryset = PropertiesModel.objects.all()
    serializer_class = PropertiesSerializer
    #permission_classes = [IsAuthenticated]

   # def get_permissions(self):
    #    if self.action == 'list' :
          #  permission_classes = [IsGetRequest]
      #  else :
       #     permission_classes = [IsAuthenticated]
        #return [permission() for permission in permission_classes]


   