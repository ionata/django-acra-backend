"""Models that store the ACRA data"""
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AcraException(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    android_version = models.CharField(max_length=255, blank=True)
    app_version_code = models.CharField(max_length=255, blank=True)
    app_version_name = models.CharField(max_length=255, blank=True)
    available_mem_size = models.BigIntegerField(default=0)
    brand = models.CharField(max_length=255, blank=True)
    build = models.TextField(blank=True)
    build_config = models.TextField(blank=True)
    crash_configuration = models.TextField(blank=True)
    custom_data = models.TextField(blank=True)
    device_features = models.TextField(blank=True)
    device_id = models.CharField(max_length=255, blank=True)
    display = models.TextField(blank=True)
    dropbox = models.TextField(blank=True)
    dumpsys_meminfo = models.TextField(blank=True)
    environment = models.TextField(blank=True)
    eventslog = models.TextField(blank=True)
    file_path = models.CharField(max_length=255, blank=True)
    initial_configuration = models.TextField(blank=True)
    installation_id = models.CharField(max_length=255, blank=True)
    is_silent = models.BooleanField(default=False)
    logcat = models.TextField(blank=True)
    media_codec_list = models.TextField(blank=True)
    package_name = models.CharField(max_length=255, blank=True)
    phone_model = models.CharField(max_length=255, blank=True)
    product = models.CharField(max_length=255, blank=True)
    radiolog = models.TextField(blank=True)
    report_id = models.CharField(max_length=255, blank=True)
    settings_global = models.TextField(blank=True)
    settings_secure = models.TextField(blank=True)
    settings_system = models.TextField(blank=True)
    shared_preferences = models.TextField(blank=True)
    stack_trace = models.TextField(blank=True)
    thread_details = models.TextField(blank=True)
    total_mem_size = models.BigIntegerField(default=0)
    user_app_start_date = models.CharField(max_length=255, blank=True)
    user_comment = models.TextField(blank=True)
    user_crash_date = models.CharField(max_length=255, blank=True)
    user_email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{} ({}, {})".format(self.created,
                                    self.app_version_code,
                                    self.android_version)
