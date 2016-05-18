#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

from djangocms_unitegallery import __version__


INSTALL_REQUIRES = [
    'django>=1.7',
    'django-cms>=3.0',
    'easy_thumbnails',
    'django-filer>=0.9.12',
    'cmsplugin-filer>=0.10.2',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Framework :: Django',
    'Framework :: Django :: 1.7',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
]


if sys.version_info >= (3, 0):
    enc = {'encoding': 'UTF-8'}
else:
    enc = {}

long_desc = r'''
%s

%s
''' % (open('README.rst', **enc).read(), open('CHANGELOG.rst', **enc).read())

setup(
    name='djangocms-unitegallery',
    version=__version__,
    description='unitegallery grid Plugin for django CMS',
    author='David Jean Louis',
    author_email='izimobil@gmail.com',
    url='https://github.com/izimobil/djangocms-unitegallery',
    packages=[
        'djangocms_unitegallery',
        'djangocms_unitegallery.migrations',
    ],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
