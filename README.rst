===================
Sites Debug Toolbar
===================

The Sites Debug Toolbar is an add-on for Django Debug Toolbar for browsing
``django.contrib.sites``. It's main intention is to debug projects using
``django.contrib.sites`` to serve multiple sites. There are several apps
which allows you to set SITE_ID dynamically according to current domain, like
django-dynamicsites_. That app comes with helpful article_ to begin with.

Installation and configuration
==============================

#. Install and configure `Django Debug Toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_.

#. Add the ``sites_toolbar`` app to your ``INSTALLED_APPS``.

#. Add the ``sites`` panel to ``DEBUG_TOOLBAR_PANELS``.

::

	DEBUG_TOOLBAR_PANELS = (
            ...
	    'sites_toolbar.panels.SitesDebugPanel',
	)

.. _django-dynamicsites: https://bitbucket.org/uysrc/django-dynamicsites/src
.. _article: http://blog.uysrc.com/2011/03/23/serving-multiple-sites-with-django/
