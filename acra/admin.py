from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import AcraException


@admin.register(AcraException)
class AcraExceptionAdmin(admin.ModelAdmin):
    list_display = [
        'android_version',
        'app_version_code',
        'brand',
        'product',
    ]
    list_filter = [
        'android_version',
        'app_version_code',
    ]
    readonly_fields = [
        'created',
        'android_version',
        'app_version_code',
        'app_version_name',
        'available_mem_size',
        'brand',
        'build',
        'crash_configuration',
        'custom_data',
        'device_features',
        'display',
        'dumpsys_meminfo',
        'environment',
        'file_path',
        'initial_configuration',
        'installation_id',
        'is_silent',
        'logcat',
        'package_name',
        'phone_model',
        'product',
        'report_id',
        'settings_global',
        'settings_secure',
        'settings_system',
        'shared_preferences',
        'stack_trace',
        'total_mem_size',
        'user_app_start_date',
        'user_comment',
        'user_crash_date',
        'user_email',
    ]
