from django.conf import settings
from django.utils.translation import gettext_lazy as _


TAB_TYPE_CHOICES = (
    ('nav-tabs', _('Tabs')),
    ('nav-pills', _('Pills')),
)

TAB_ALIGNMENT_CHOICES = (
    ('nav-fill', _('Fill')),
    ('nav-justified', _('Justified')),
    ('justify-content-start', _('Justify start')),
    ('justify-content-center', _('Justify center')),
    ('justify-content-end', _('Justify end')),
    ('flex-column', _('Column')),
)

TAB_EFFECT_CHOICES = (
    ('fade', _('Fade')),
)

TAB_TEMPLATE_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP5_TAB_TEMPLATES',
    (
        ('default', _('Default')),
    ),
)
