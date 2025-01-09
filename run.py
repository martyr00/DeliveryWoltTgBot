import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import API_KEY
from language import set_locale, get_language_keyboard, LANGUAGES, set_user_language, get_user_language
from main_menu import get_main_menu, handle_faq, handle_cabinet

bot = Bot(token=API_KEY)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    """
    Handles the /start command.
    """
    await message.answer(
        "Choose a language:",
        reply_markup=get_language_keyboard()
    )


@dp.callback_query(lambda call: call.data.startswith("lang_"))
async def set_language(callback_query: CallbackQuery):
    """
    Handles language selection.
    """
    lang_code = callback_query.data.split("_")[1]
    set_user_language(callback_query.from_user.id, lang_code)
    _ = set_locale(lang_code)

    # Update the message to confirm language selection
    await callback_query.message.edit_text(
        _("Language set to {lang_name}!").format(lang_name=LANGUAGES[lang_code])
    )

    # Send the main menu
    await callback_query.message.answer(
        _("Main menu:"),
        reply_markup=get_main_menu(callback_query.from_user.id)
    )


@dp.callback_query(lambda call: call.data == "menu_back")
async def menu_back(callback_query: CallbackQuery):
    """
    Handles the Back button click, returning to the main menu.
    """
    lang_code = get_user_language(callback_query.from_user.id)
    _ = set_locale(lang_code)

    # Replace the Cabinet menu with the main menu
    await callback_query.message.edit_text(
        _("Main menu:"),
        reply_markup=get_main_menu(callback_query.from_user.id)
    )


@dp.callback_query(lambda call: call.data == "menu_cabinet")
async def menu_cabinet(callback_query: CallbackQuery):
    """
    Handles the Cabinet button click.
    """
    await handle_cabinet(callback_query, bot)


@dp.callback_query(lambda call: call.data == "menu_faq")
async def menu_faq(callback_query: CallbackQuery):
    """
    Handles the FAQ button click.
    """
    await handle_faq(callback_query, bot)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
