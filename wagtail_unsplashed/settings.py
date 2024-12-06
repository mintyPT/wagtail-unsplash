from django.conf import settings

DEFAULTS = {}


class WagtailUnsplashSettings:
    def __getattr__(self, attr):
        django_settings = getattr(settings, "WAGTAIL_UNSPLASHED", {})

        try:
            return django_settings[attr]
        except KeyError:
            return getattr(DEFAULTS, attr, None)


wagtail_unsplashed_settings = WagtailUnsplashSettings()
