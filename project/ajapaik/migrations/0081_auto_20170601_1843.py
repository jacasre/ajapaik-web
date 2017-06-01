# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik', '0080_auto_20170601_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dating',
            name='comment_obj',
            field=models.OneToOneField(related_name='datings', null=True, blank=True, to='ajapaik.MyXtdComment'),
        ),
    ]
