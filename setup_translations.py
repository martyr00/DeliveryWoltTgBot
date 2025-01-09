import gettext
from aiogram import Dispatcher

LANGUAGES = {"en": "English", "ru": "Русский"}


def setup_translations(dp: Dispatcher):
    global _
    user_language = dp.data.get("language", "en")
    translation = gettext.translation(
        'messages', localedir='locales', languages=[user_language], fallback=True
    )
    translation.install()
    _ = translation.gettext