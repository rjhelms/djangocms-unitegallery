# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible
from cmsplugin_filer_utils import FilerPluginManager
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.folder import FilerFolderField
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

    class Meta:
        verbose_name = _("Photo")

    def __str__(self):
        if self.image.name:
            return self.image.name
        else:
            return self.image.original_filename

# Models for supporting galleries made from folders


@python_2_unicode_compatible
class GalleryFolder(CMSPlugin):
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
    folder = FilerFolderField(verbose_name=_("Photo folder"))

    translatable_content_excluded_fields = ['options', 'theme']

    objects = FilerPluginManager(select_related=('folder',))

    def __str__(self):
        return self.get_theme_display()

    def clean(self):
        if self.options:
            try:
                json.loads(self.options)
            except ValueError:
                raise ValidationError('You must provide a valid JSON string')
