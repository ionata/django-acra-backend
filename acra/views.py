from __future__ import absolute_import, print_function, unicode_literals

import json

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .decorators import basicauth
from .models import AcraException


@csrf_exempt
@basicauth
@permission_required('acra.add_acraexception')
def create_report_exception(request):
    if request.method != "POST":
        raise PermissionDenied()
    data = json.loads(request.body.decode('utf-8'))
    exception = AcraException()
    for key in data.keys():
        if key.lower() in ['created', 'pk']:
            continue
        value = _booleanise(data[key])
        setattr(exception, key.lower(), value)
    exception.save()
    return HttpResponse(status=201)


def _booleanise(value):
    """Try to booleanise something, return it unchanged if not possible"""
    try:
        if value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
    except (AttributeError, TypeError):
        pass
    return value
