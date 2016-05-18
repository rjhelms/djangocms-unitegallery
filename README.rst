djangocms-unitegallery
======================

.. image:: https://travis-ci.org/rjhelms/djangocms-unitegallery.svg?branch=master
    :target: https://travis-ci.org/rjhelms/djangocms-unitegallery

.. image:: https://img.shields.io/pypi/l/djangocms-unitegallery.svg

.. image:: https://img.shields.io/pypi/pyversions/djangocms-unitegallery.svg

.. image:: https://img.shields.io/badge/django-1.7%20or%20newer-green.svg

.. image:: https://img.shields.io/badge/djangocms-3%20or%20newer-green.svg

.. image:: https://img.shields.io/pypi/dm/djangocms-unitegallery.svg


A gallery plugin for django CMS that uses the excellent
`Unite Gallery <http://unitegallery.net>`_ jQuery plugin.


Installation
------------

This plugin requires `django CMS` 3.0 or higher and `sorl-thumbnail`
12.0 or higher to work.

* Run ``pip install djangocms-unitegallery``
* Add ``'sorl.thumbnail'`` and ``'djangocms_unitegallery'`` to your ``INSTALLED_APPS``
* Run ``python manage.py migrate``

.. note::
    It's up to you to include jQuery js file in your templates, just make
    sure you include it **before** the sekizai ``{% render_block js %}``.
  

Configuration
-------------

By default djangocms-unitegallery generates thumbnails for better perfomance.
The default behavior is to generate thumbnails by resizing and cropping images
in a square of 250x250 px.

You can disable completely the thumbnail generation and leave Unite Gallery
handles images and preview, or you can change the default size of generated
thumbnails and/or wether the image ratio should be preserved or not::

    DJANGOCMS_UNITEGALLERY_CONFIG = {
        'THUMBNAIL_ENABLED': true,
        'THUMBNAIL_MAX_WIDTH': 250,
        'THUMBNAIL_MAX_HEIGHT': 250,
        'THUMBNAIL_PRESERVE_RATIO': False, 
    }

If you set ``THUMBNAIL_PRESERVE_RATIO`` to ``False``, thumbnails will be
cropped to match the configured width and height.
If you set ``THUMBNAIL_PRESERVE_RATIO`` to ``True``, thumbnails
will just be resized to match the configured max width (if image is landscape)
or height (if image is portrait).

.. note::
    Due to Unite Gallery behavior, and depending on configured options, you
    are not guaranteed to have the thumbnail size you configured in settings.
