# -*- coding: utf-8 -*-

from django.contrib.admin import TabularInline, StackedInline
from .models import GalleryPhoto


class PhotoInline(StackedInline):
    """
    Tabular inline that will be displayed in the gallery form during frontend
    editing or in the admin site.
    """
    model = GalleryPhoto
    fk_name = "gallery"
