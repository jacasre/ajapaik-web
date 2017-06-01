# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajapaik', '0077_auto_20170420_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='myxtdcomment',
            name='comment_type',
            field=models.PositiveSmallIntegerField(default=1, choices=[(0, '\u0423\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0434\u0430\u0442\u044b'), (1, 'Standard')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(max_length=2047, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_de',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_et',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_fi',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_nl',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_no',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name_sv',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='open',
            field=models.BooleanField(default=False, verbose_name='Is open'),
        ),
        migrations.AlterField(
            model_name='dating',
            name='end_accuracy',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, '\u0414\u0435\u043d\u044c'), (1, '\u041c\u0435\u0441\u044f\u0446'), (2, '\u0413\u043e\u0434')]),
        ),
        migrations.AlterField(
            model_name='dating',
            name='start_accuracy',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, '\u0414\u0435\u043d\u044c'), (1, '\u041c\u0435\u0441\u044f\u0446'), (2, '\u0413\u043e\u0434')]),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='map_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, '\u0413\u0443\u0433\u043b \u041a\u0430\u0440\u0442\u0430'), (1, 'Google satellite'), (2, 'OpenStreetMap'), (3, 'Juks'), (4, '\u041d\u0435\u0442 \u043a\u0430\u0440\u0442\u044b')]),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='origin',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, '\u0418\u0433\u0440\u0430'), (1, '\u041a\u0430\u0440\u0442\u0430'), (2, '\u0413\u0430\u043b\u0435\u0440\u0435\u044f'), (3, '\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u0430\u044f \u0441\u0441\u044b\u043b\u043a\u0430'), (4, '\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a')]),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, '\u041a\u0430\u0440\u0442\u0430'), (1, 'EXIF'), (2, 'GPS'), (3, '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435'), (4, 'StreetView'), (5, 'Source geotag')]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.CharField(max_length=255, null=True, verbose_name='Author', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_de',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_en',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_et',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_fi',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_nl',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_no',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description_sv',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'uploads', max_length=255, blank=True, null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='points',
            name='action',
            field=models.PositiveSmallIntegerField(db_index=True, choices=[(0, '\u0413\u0435\u043e\u0442\u044d\u0433'), (1, '\u041f\u0435\u0440\u0435\u0441\u043d\u0438\u043c\u043e\u043a'), (2, '\u0417\u0430\u043a\u0430\u0447\u0430\u0442\u044c \u0444\u043e\u0442\u043e'), (3, '\u0424\u043e\u0442\u043e \u043a\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'), (4, 'Photo re-curation'), (5, '\u0423\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0434\u0430\u0442\u044b'), (6, '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u0434\u0430\u0442\u044b'), (7, '\u041f\u043b\u0435\u043d\u043a\u0430')]),
        ),
        migrations.AlterField(
            model_name='tour',
            name='photo_set_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, 'Open tour'), (0, 'Fixed photo set'), (2, 'Random with nearby pictures')]),
        ),
    ]
