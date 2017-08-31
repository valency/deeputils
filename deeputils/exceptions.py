from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException


class BadRequest(APIException):
    status_code = 400
    default_detail = _('This field may not be empty.')


class Unauthorized(APIException):
    status_code = 401
    default_detail = _('The requested user is not authorized.')


class Forbidden(APIException):
    status_code = 403
    default_detail = _('The requested user is not authorized to access certain API.')


class NotFound(APIException):
    status_code = 404
    default_detail = _('Not found.')


class NotAcceptable(APIException):
    status_code = 406
    default_detail = _('This field value is not acceptable according to its definition.')


class Conflict(APIException):
    status_code = 409
    default_detail = _('This field value is unique but already exists.')
