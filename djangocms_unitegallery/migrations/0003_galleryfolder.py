# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0005_auto_20160518_1525'),
        ('djangocms_unitegallery', '0002_auto_20160518_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='cms.CMSPlugin', primary_key=True)),
                ('theme', models.CharField(max_length=20, choices=[('default', 'Default'), ('carousel', 'Carousel'), ('compact', 'Compact'), ('grid', 'Grid'), ('slider', 'Slider'), ('tiles', 'Tiles'), ('tilesgrid', 'Tiles grid')], default='default', verbose_name='Theme')),
                ('options', models.TextField(blank=True, verbose_name='Theme options', help_text='This field allow you to pass a JSON object if you want to customize the gallery. Please consult the Unite gallery docs for a list of options.')),
                ('folder', filer.fields.folder.FilerFolderField(to='filer.Folder', verbose_name='Photo folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
