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
        'get_stacktrace_str',
        'get_logging_str',
        'created',
        'android_version',
        'app_version_code',
        'app_version_name',
        'available_mem_size',
        'brand',
        'build',
        'build_config',
        'crash_configuration',
        'custom_data',
        'device_features',
        'device_id',
        'display',
        'dropbox',
        'dumpsys_meminfo',
        'environment',
        'eventslog',
        'file_path',
        'initial_configuration',
        'installation_id',
        'is_silent',
        'logcat',
        'media_codec_list',
        'package_name',
        'phone_model',
        'product',
        'report_id',
        'radiolog',
        'settings_global',
        'settings_secure',
        'settings_system',
        'shared_preferences',
        'stack_trace',
        'thread_details',
        'total_mem_size',
        'user_app_start_date',
        'user_comment',
        'user_crash_date',
        'user_email',
    ]
    fieldsets = [
        ['Basic information', {
            'fields': [
                'created',
                'android_version',
                'app_version_code',
                'app_version_name',
                'available_mem_size',
                'brand',
                'file_path',
                'installation_id',
                'is_silent',
                'package_name',
                'phone_model',
                'product',
                'report_id',
                'total_mem_size',
                'user_app_start_date',
                'user_comment',
                'user_crash_date',
                'user_email',
        ]}],
        ['Trace', {
            'fields': [
                'get_stacktrace_str',
        ]}],
        ['Logging', {
            'fields': [
                'get_logging_str',
            ],
            'classes': ['collapse'],
        }],
        ['Other', {
            'fields': [
                'build',
                'build_config',
                'crash_configuration',
                'custom_data',
                'device_features',
                'device_id',
                'display',
                'dropbox',
                'dumpsys_meminfo',
                'environment',
                'eventslog',
                'initial_configuration',
                'media_codec_list',
                'radiolog',
                'settings_global',
                'settings_secure',
                'settings_system',
                'shared_preferences',
                'thread_details',
            ],
            'classes': ['collapse'],
        }]
    ]

    def get_stacktrace_str(self, obj):
        return obj.stack_trace.replace('\n', '<br>').replace('\t', 4 * '&nbsp;')
    get_stacktrace_str.allow_tags = True
    get_stacktrace_str.short_description = 'Stack trace'

    def get_logging_str(self, obj):
        return obj.logcat.replace('\n', '<br>').replace('\t', 4 * '&nbsp;')
    get_logging_str.allow_tags = True
    get_logging_str.short_description = 'Logcat'
