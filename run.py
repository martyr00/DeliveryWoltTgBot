import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import API_KEY
from language import set_locale, get_language_keyboard, LANGUAGES, set_user_language, get_user_language

bot = Bot(token=API_KEY)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    """
    Обрабатывает команду /start.
    """
    await message.answer(
        "Выберите язык / Choose a language:",
        reply_markup=get_language_keyboard()
    )


@dp.callback_query(lambda call: call.data.startswith("lang_"))
async def set_language(callback_query: CallbackQuery):
    """
    Обрабатывает выбор языка.
    """
    lang_code = callback_query.data.split("_")[1]
    set_user_language(callback_query.from_user.id, lang_code)
    _ = set_locale(lang_code)

    await callback_query.message.edit_text(
        _("Language set to {lang_name}!").format(lang_name=LANGUAGES[lang_code])
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
