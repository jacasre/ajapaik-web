# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-09 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik_face_recognition', '0094_auto_20190716_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facerecognitionrectangle',
            name='facePhoto',
        ),
        migrations.AddField(
            model_name='facerecognitionrectangle',
            name='subjectPhoto',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='uploads', verbose_name='SubjectPhoto'),
        ),
    ]