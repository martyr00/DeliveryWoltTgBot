import gettext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

LANGUAGES = {
    "en": "English 🇬🇧",
    "ru": "Русский 🇷🇺",
}

user_languages = {}


def set_locale(lang_code: str):
    """
    Устанавливает локаль для выбранного языка.
    """
    translation = gettext.translation(
        "messages", localedir="locales", languages=[lang_code], fallback=True
    )
    translation.install()
    return translation.gettext


def get_language_keyboard():
    """
    Возвращает клавиатуру для выбора языка.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f"lang_{code}")]
            for code, name in LANGUAGES.items()
        ]
    )
    return keyboard


def get_user_language(user_id: int):
    """
    Получает язык пользователя. По умолчанию `en`.
    """
    return user_languages.get(user_id, "en")


def set_user_language(user_id: int, lang_code: str):
    """
    Устанавливает язык для конкретного пользователя.
    """
    user_languages[user_id] = lang_code
