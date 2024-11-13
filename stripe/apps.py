from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Python package 'stripe' is not installed.")


class StripeApp2(AppConfig):
    default = True
    name = 'pretix.plugins.stripe2'
    verbose_name = _("Stripe2")

    class PretixPluginMeta:
        name = _("Stripe2")
        author = "eventyay"
        version = __version__
        category = 'PAYMENT'
        featured = True
        visible = True
        description = _("This plugin allows you to receive credit card payments " +
                        "via Stripe.")

    def ready(self):
        from . import signals, tasks  # NOQA


default_app_config = 'pretix.plugins.stripe2.StripeApp2'
