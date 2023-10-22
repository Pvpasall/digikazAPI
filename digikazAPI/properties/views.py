from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsGetRequest
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import PropertiesSerializer
from .models import PropertiesModel


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = PropertiesModel.objects.all()
    serializer_class = PropertiesSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsGetRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(
        operation_description="Create properties",
        responses={201: openapi.Response("Property created", PropertiesSerializer)},
        response_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "exampleTest": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Example description"
                ),
            },
            required=["exampleTest"],
        ),
    )
    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

    def retrieve(self, request, *args, **kwargs):
        property_id = kwargs.get("pk")
        property = get_object_or_404(PropertiesModel, pk=property_id)

        serializer = self.get_serializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        property_id = kwargs["pk"]
        property = get_object_or_404(PropertiesModel, pk=property_id)

        serializer = self.get_serializer(property, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        property_id = kwargs["pk"]
        property = get_object_or_404(PropertiesModel, pk=property_id)

        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
