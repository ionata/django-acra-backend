"""HTTP Basic Auth. Adapted from https://gist.github.com/codeinthehole/4732233"""
from __future__ import absolute_import, print_function, unicode_literals

import base64
from functools import wraps

from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate


def _get_request_auth(request):
    auth = request.META.get('HTTP_AUTHORIZATION', None)
    if auth is not None:
        return auth.split()


def _request_has_auth(request):
    auth = _get_request_auth(request)
    return auth is not None and auth[0].lower() == 'basic'


def _unpack_auth(auth):
    return base64.b64decode(auth[1]).decode('utf-8').strip().split(':')


def _user_from_auth(auth):
    credentials = _unpack_auth(auth)
    return authenticate(username=credentials[0], password=credentials[1])


def _get_request_auth_user(request):
    return _user_from_auth(_get_request_auth(request))


def basicauth(view):
    @wraps(view)
    def _basic_auth(request, *args, **kwargs):
        if _request_has_auth(request):
            user = _get_request_auth_user(request)
            if user is not None and user.is_active:
                request.user = user
                return view(request, *args, **kwargs)
        raise PermissionDenied()
    return _basic_auth
