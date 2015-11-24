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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('android_version', models.CharField(blank=True, max_length=255)),
                ('app_version_code', models.CharField(blank=True, max_length=255)),
                ('app_version_name', models.CharField(blank=True, max_length=255)),
                ('available_mem_size', models.BigIntegerField(default=0)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('build', models.TextField(blank=True)),
                ('build_config', models.TextField(blank=True)),
                ('crash_configuration', models.TextField(blank=True)),
                ('custom_data', models.TextField(blank=True)),
                ('device_features', models.TextField(blank=True)),
                ('device_id', models.CharField(blank=True, max_length=255)),
                ('display', models.TextField(blank=True)),
                ('dropbox', models.TextField(blank=True)),
                ('dumpsys_meminfo', models.TextField(blank=True)),
                ('environment', models.TextField(blank=True)),
                ('eventslog', models.TextField(blank=True)),
                ('file_path', models.CharField(blank=True, max_length=255)),
                ('initial_configuration', models.TextField(blank=True)),
                ('installation_id', models.CharField(blank=True, max_length=255)),
                ('is_silent', models.BooleanField(default=False)),
                ('logcat', models.TextField(blank=True)),
                ('media_codec_list', models.TextField(blank=True)),
                ('package_name', models.CharField(blank=True, max_length=255)),
                ('phone_model', models.CharField(blank=True, max_length=255)),
                ('product', models.CharField(blank=True, max_length=255)),
                ('radiolog', models.TextField(blank=True)),
                ('report_id', models.CharField(blank=True, max_length=255)),
                ('settings_global', models.TextField(blank=True)),
                ('settings_secure', models.TextField(blank=True)),
                ('settings_system', models.TextField(blank=True)),
                ('shared_preferences', models.TextField(blank=True)),
                ('stack_trace', models.TextField(blank=True)),
                ('thread_details', models.TextField(blank=True)),
                ('total_mem_size', models.BigIntegerField(default=0)),
                ('user_app_start_date', models.CharField(blank=True, max_length=255)),
                ('user_comment', models.TextField(blank=True)),
                ('user_crash_date', models.CharField(blank=True, max_length=255)),
                ('user_email', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
