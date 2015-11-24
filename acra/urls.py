from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from .views import create_report_exception


urlpatterns = [
    url(r'^$', create_report_exception, name='acra-report-exception'),
]
