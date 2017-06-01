# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik', '0079_dating_comment_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dating',
            name='comment_obj',
            field=models.OneToOneField(null=True, blank=True, to='ajapaik.MyXtdComment'),
        ),
    ]
