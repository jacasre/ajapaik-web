# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ajapaik', '0081_auto_20170601_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verb', models.PositiveSmallIntegerField(choices=[(0, 'Commented'), (1, 'Added geotag')])),
                ('action_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('target_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('action_content_type', models.ForeignKey(related_name='action_notifcation', to='contenttypes.ContentType')),
                ('receivers', models.ManyToManyField(related_name='notifications', to='ajapaik.Profile')),
                ('sender', models.ForeignKey(to='ajapaik.Profile')),
                ('target_content_type', models.ForeignKey(related_name='target_notifcation', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'db_table': 'project_notification',
            },
        ),
    ]
