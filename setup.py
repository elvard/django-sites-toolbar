#!/usr/bin/env python
# -*- encoding: utf8 -*-
from setuptools import setup

from sites_toolbar import __version__

setup(
    name='django-sites-toolbar',
    version=__version__,
    description=
        'Django debug-toolbar panel for browsing available django.contrib.sites',
    author='Tomáš Ehrlich',
    author_email='tomas.ehrlich@gmail.com',
    url='https://github.com/elvard/django-sites-toolbar',
    download_url='https://github.com/downloads/elvard/django-sites-toolbar/django-sites-toolbar-0.1a.tar.gz',
    packages=['sites_toolbar'],
    license='GPL v3',
    package_data={'sites_toolbar': ['templates/sites_toolbar/*']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
