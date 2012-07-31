import os.path

from django.conf import settings
from django.contrib.sites.models import Site
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import DebugPanel


class SiteDebugPanel(DebugPanel):
    """
    Panel that displays informations about Sites
    """
    name = 'Site'
    template = 'sites_toolbar/panel.html'
    has_content = True

    def nav_title(self):
        return _('Sites')

    def nav_subtitle(self):
        site = Site.objects.get(id=settings.SITE_ID)
        return '%s' % site.name

    def url(self):
        return ''

    def title(self):
        return _('Sites')

    def process_response(self, request, response):
        sites = []
        for s in Site.objects.all():
            site = model_to_dict(s)
            site['folder_name'] = os.path.realpath(
                    os.path.join(settings.SITES_DIR, site['folder_name']))
            sites.append(site)

        self.record_stats({
            'sites': sites,
            'current_site_id': settings.SITE_ID 
        })
