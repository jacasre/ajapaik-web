# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik', '0078_auto_20170601_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='dating',
            name='comment_obj',
            field=models.ForeignKey(blank=True, to='ajapaik.MyXtdComment', null=True),
        ),
    ]
