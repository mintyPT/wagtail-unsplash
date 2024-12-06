from wagtail_unsplashed.settings import wagtail_unsplashed_settings

from unsplash.api import Api
from unsplash.auth import Auth

api = Api(
    Auth(
        wagtail_unsplashed_settings.CLIENT_ID,
        wagtail_unsplashed_settings.CLIENT_SECRET,
        wagtail_unsplashed_settings.REDIRECT_URI,
        code=wagtail_unsplashed_settings.CODE,
    )
)
