# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_unitegallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='galleryphoto',
            name='title',
        ),
        migrations.AlterField(
            model_name='galleryphoto',
            name='image',
            field=filer.fields.image.FilerImageField(verbose_name='Photo', to='filer.Image'),
        ),
    ]
