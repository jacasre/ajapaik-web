# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-29 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik', '0113_transcriptionfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptionfeedback',
            name='transcription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcription', to='ajapaik.Transcription'),
            preserve_default=False,
        ),
    ]
