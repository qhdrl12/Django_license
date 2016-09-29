from rest_framework import response, schemas, viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger .renderers import OpenAPIRenderer, SwaggerUIRenderer

from django.contrib.auth.models import User, Group
from Django_license.serializers import UserSerializers, GroupSerializers

@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='license API')
    return response.Response(generator.get_schema(request=request))

class UserViewSet(viewsets.ModelViewSet):
    """
    User API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers