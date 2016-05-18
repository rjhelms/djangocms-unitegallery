# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField

from .settings import DJANGOCMS_UNITEGALLERY_CONFIG as CONFIG


CONFIG.update(getattr(settings, 'DJANGOCMS_UNITEGALLERY_CONFIG', {}))

GALLERY_THEMES = (
    ('default', 'Default'),
    ('carousel', 'Carousel'),
    ('compact', 'Compact'),
    ('grid', 'Grid'),
    ('slider', 'Slider'),
    ('tiles', 'Tiles'),
    ('tilesgrid', 'Tiles grid'),
)


def get_media_path(instance, filename):
    return instance.gallery.get_media_path(filename)


@python_2_unicode_compatible
class Gallery(CMSPlugin):
    theme = models.CharField(
        _('Theme'),
        max_length=20,
        choices=GALLERY_THEMES,
        default=GALLERY_THEMES[0][0],
    )
    options = models.TextField(
        _('Theme options'),
        blank=True,
        help_text=_(
            'This field allow you to pass a JSON object if you want to '
            'customize the gallery. Please consult the Unite gallery docs '
            'for a list of options.'
        )
    )
    translatable_content_excluded_fields = ['options', 'theme']

    def __str__(self):
        return self.get_theme_display()

    def copy_relations(self, old_instance):
        for photo in old_instance.photos.all():
            new_photo = GalleryPhoto(
                image=photo.image,
                title=photo.title,
                description=photo.description,
                gallery=self
            )
            new_photo.save()

    def clean(self):
        if self.options:
            try:
                json.loads(self.options)
            except ValueError:
                raise ValidationError('You must provide a valid JSON string')


@python_2_unicode_compatible
class GalleryPhoto(models.Model):
    image = FilerImageField(verbose_name=_("Photo"))

    gallery = models.ForeignKey(
        Gallery,
        verbose_name=_("Gallery"),
        related_name="photos"
    )

    def __str__(self):
        return self.image.name

    def get_thumbnail_size(self):
        """
        Returns a string representing the size of the thumbnail, suitable
        for easy-thumbnail, eg.: '150x0', '0x200', '200x200', etc.
        """
        if not self.image or not CONFIG['THUMBNAIL_ENABLED']:
            return False
        if CONFIG['THUMBNAIL_PRESERVE_RATIO']:
            if self.image.height > self.image.width:
                ret = '0x%s' % CONFIG['THUMBNAIL_MAX_HEIGHT']
            else:
                ret = '%sx0' % CONFIG['THUMBNAIL_MAX_WIDTH']
        else:
            ret = '%sx%s' % (
                CONFIG['THUMBNAIL_MAX_WIDTH'], CONFIG['THUMBNAIL_MAX_HEIGHT']
            )
        return ret
