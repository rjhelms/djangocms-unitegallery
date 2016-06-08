# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from filer.models import Image

from .admin import PhotoInline
from .models import Gallery, GalleryFolder, CONFIG


class GalleryPlugin(CMSPluginBase):
    """
    The gallery plugin instance.
    """
    model = Gallery
    name = _('Gallery')
    module = _('Unite gallery')
    render_template = 'djangocms_unitegallery/gallery.html'
    inlines = [PhotoInline, ]

    def render(self, context, instance, placeholder):
        context.update({
            'gallery': instance,
            'placeholder': placeholder,
            'CONFIG': CONFIG
        })
        return context


class GalleryFolderPlugin(CMSPluginBase):
    """
    The gallery folder plugin instance
    """
    model = GalleryFolder
    name = _('Gallery Folder')
    module = _('Unite gallery')
    render_template = 'djangocms_unitegallery/galleryfolder.html'

    def render(self, context, instance, placeholder):
        context.update({
            'gallery': instance,
            'photos': Image.objects.filter(folder__id=instance.folder.pk),
            'placeholder': placeholder,
            'CONFIG': CONFIG
        })
        return context

plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(GalleryFolderPlugin)
