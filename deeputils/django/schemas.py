import coreapi
from rest_framework import serializers
from rest_framework.schemas import AutoSchema
from rest_framework.schemas.inspectors import field_to_schema
from rest_framework.viewsets import GenericViewSet


class RefinedViewSchema(AutoSchema):
    def get_fields(self, method):
        fields = []
        for field in self.view.get_serializer().fields.values():
            if not field.read_only and not isinstance(field, serializers.HiddenField):
                fields.append(coreapi.Field(
                    name=field.field_name,
                    location='form',
                    required=field.required and method != 'PATCH',
                    schema=field_to_schema(field)
                ))
        return fields

    def get_link(self, path, method, base_url):
        link = super().get_link(path, method, base_url)
        if method == 'GET':
            link._fields = tuple(self.get_fields(method))
            link._encoding = 'path'
        elif method == 'DELETE':
            link._fields = tuple(self.get_fields(method))
            link._encoding = 'application/json'
        return link


class RefinedViewSet(GenericViewSet):
    schema = RefinedViewSchema()
    serializer_classes = {
        'list': None,
        'create': None,
        'update': None,
        'destroy': None
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]
