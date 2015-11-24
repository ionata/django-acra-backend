# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcraException',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('android_version', models.CharField(max_length=255, blank=True)),
                ('app_version_code', models.CharField(max_length=255, blank=True)),
                ('app_version_name', models.CharField(max_length=255, blank=True)),
                ('available_mem_size', models.BigIntegerField(default=0)),
                ('brand', models.CharField(max_length=255, blank=True)),
                ('build', models.TextField(blank=True)),
                ('crash_configuration', models.TextField(blank=True)),
                ('custom_data', models.TextField(blank=True)),
                ('device_features', models.TextField(blank=True)),
                ('display', models.TextField(blank=True)),
                ('dumpsys_meminfo', models.TextField(blank=True)),
                ('environment', models.TextField(blank=True)),
                ('file_path', models.CharField(max_length=255, blank=True)),
                ('initial_configuration', models.TextField(blank=True)),
                ('installation_id', models.CharField(max_length=255, blank=True)),
                ('is_silent', models.BooleanField(default=False)),
                ('logcat', models.TextField(blank=True)),
                ('package_name', models.CharField(max_length=255, blank=True)),
                ('phone_model', models.CharField(max_length=255, blank=True)),
                ('product', models.CharField(max_length=255, blank=True)),
                ('report_id', models.CharField(max_length=255, blank=True)),
                ('settings_global', models.TextField(blank=True)),
                ('settings_secure', models.TextField(blank=True)),
                ('settings_system', models.TextField(blank=True)),
                ('shared_preferences', models.TextField(blank=True)),
                ('stack_trace', models.TextField(blank=True)),
                ('total_mem_size', models.BigIntegerField(default=0)),
                ('user_app_start_date', models.CharField(max_length=255, blank=True)),
                ('user_comment', models.TextField(blank=True)),
                ('user_crash_date', models.CharField(max_length=255, blank=True)),
                ('user_email', models.CharField(max_length=255, blank=True)),
            ],
        ),
    ]
