===================
Sites Debug Toolbar
===================

The Sites Debug Toolbar is an add-on for Django Debug Toolbar for browsing
``django.contrib.sites`` monkey-patched by django-dynamicsites_. That app
comes with helpful article_ to begin with. It sets SITE_ID dynamically
according to domain.

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
