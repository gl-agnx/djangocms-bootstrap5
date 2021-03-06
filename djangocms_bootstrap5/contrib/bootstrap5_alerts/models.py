from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap5.constants import COLOR_STYLE_CHOICES
from djangocms_bootstrap5.fields import AttributesField, TagTypeField


class Bootstrap5Alerts(CMSPlugin):
    """
    Components > "Alerts" Plugin
    https://getbootstrap.com/docs/5.0/components/alerts/
    """
    alert_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        default=COLOR_STYLE_CHOICES[0][0],
        max_length=255,
    )
    alert_dismissable = models.BooleanField(
        verbose_name=_('Dismissable'),
        default=False,
        help_text=_('Allows the alert to be closed.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.alert_context)
