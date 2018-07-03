import json
from json.decoder import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.serializers import empty


def validate_id(model, account, oid, allow_none=True):
    if oid is not None:
        try:
            obj = model.objects.get(pk=oid)
            if getattr(model, 'public', False) and obj.public is True:
                pass
            elif account is not None and obj.account != account:
                raise serializers.ValidationError(NotAuthenticated.default_detail)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(NotFound.default_detail)
    elif not allow_none:
        raise serializers.ValidationError(NotFound.default_detail)
    return oid


class ArrayField(serializers.CharField):
    def to_representation(self, data):
        return data.split(',') if data is not None else None

    def to_internal_value(self, data):
        return data.split(',') if data is not None else None


class JSONField(serializers.CharField):
    def run_validation(self, data=empty):
        if data is not empty and data is not None:
            try:
                json.loads(data)
            except JSONDecodeError:
                raise ValidationError("Data is not in JSON type.")
        return super().run_validation(data)

    def to_representation(self, data):
        return json.loads(data) if data is not None else None


class ModifyModelSerializer(serializers.ModelSerializer):
    def __init__(self, meta_model, meta_fields, *args, **kwargs):
        class ExtendMeta:
            model = meta_model
            fields = tuple(meta_fields)

        self.Meta = ExtendMeta()
        super().__init__(*args, **kwargs)


class ModifyViewSerializer(serializers.Serializer):
    field = serializers.CharField(help_text='Fields to be modified, separated by comma')
    value = serializers.CharField(help_text='Desired values of the modified fields, separated by comma')

    def validate_field(self, value):
        for val in value.split(','):
            if val not in self.allowed_fields:
                raise serializers.ValidationError('This field must be chosen from: ' + str(self.allowed_fields))
        return value

    def validate(self, data):
        field_list = [i.strip() for i in data['field'].split(',')]
        value_list = [i.strip() for i in data['value'].split(',')]
        if len(field_list) != len(value_list):
            raise serializers.ValidationError('The lengths of fields and values do not match.')
        del data['field']
        del data['value']
        data = {**data, **dict(zip(field_list, value_list))}
        # Fix data format issues
        data = self.fix_boolean(data)
        data = self.fix_empty(data)
        data = self.extend_validate(data)
        # Avoid the strange null id problem
        oid = None
        if 'id' in data:
            oid = data['id']
            del data['id']
        # Apply modify model serializer
        pp = ModifyModelSerializer(data=data, meta_model=self.model, meta_fields=data.keys())
        # Restore the original id
        if oid is not None:
            data['id'] = oid
        # Continue
        if pp.is_valid():
            return data
        else:
            raise serializers.ValidationError(pp.errors)

    def fix_boolean(self, data):
        for field, value in data.items():
            if type(self.model._meta.get_field(field)) == models.fields.BooleanField:
                data[field] = value.capitalize()
        return data

    def fix_empty(self, data):
        for field, value in data.items():
            if value == '':
                data[field] = None
        return data

    def extend_validate(self, data):
        return data


class ObjectPutViewSerializer(ModifyViewSerializer):
    id = serializers.IntegerField(help_text='Object ID')

    def __init__(self, model=None, account=None, allowed_fields=tuple(), *args, **kwargs):
        self.model = model
        self.account = account
        self.allowed_fields = allowed_fields
        super().__init__(*args, **kwargs)

    def validate_id(self, value):
        return validate_id(self.model, self.account, value)


class ObjectPostViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text='Object ID', required=False)

    def __init__(self, model=None, account=None, *args, **kwargs):
        self.model = model
        self.account = account
        super().__init__(*args, **kwargs)

    def validate_id(self, value):
        if value is not None:
            try:
                self.model.objects.get(pk=value)
                raise serializers.ValidationError('Content is conflict.')
            except ObjectDoesNotExist:
                pass
        return value


class ObjectGetViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text='Object ID', required=False)

    def __init__(self, model=None, account=None, *args, **kwargs):
        self.model = model
        self.account = account
        super().__init__(*args, **kwargs)

    def validate_id(self, value):
        return validate_id(self.model, self.account, value)


class ObjectDeleteViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text='Object ID')

    def __init__(self, model=None, account=None, *args, **kwargs):
        self.model = model
        self.account = account
        super().__init__(*args, **kwargs)

    def validate_id(self, value):
        return validate_id(self.model, self.account, value, False)
