from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from language import set_locale, get_user_language


def get_main_menu(user_id: int):
    """
    Returns the main menu with localized texts.
    """
    lang_code = get_user_language(user_id)
    _ = set_locale(lang_code)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("FAQ"), callback_data="menu_faq")],
            [InlineKeyboardButton(text=_("Cabinet"), callback_data="menu_cabinet")],
        ]
    )
    return keyboard


def get_cabinet_menu(user_id: int):
    """
    Returns the cabinet menu with a back button.
    """
    lang_code = get_user_language(user_id)
    _ = set_locale(lang_code)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("Back"), callback_data="menu_back")],
        ]
    )
    return keyboard


async def handle_faq(callback_query, bot):
    """
    Handles the FAQ button click.
    """
    pass


async def handle_cabinet(callback_query, bot):
    """
    Handles the Cabinet button click, replacing the main menu with the cabinet menu.
    """
    lang_code = get_user_language(callback_query.from_user.id)
    _ = set_locale(lang_code)

    # Replace the main menu with the Cabinet menu
    await callback_query.message.edit_text(
        _("Welcome to your cabinet!"),
        reply_markup=get_cabinet_menu(callback_query.from_user.id)
    )
