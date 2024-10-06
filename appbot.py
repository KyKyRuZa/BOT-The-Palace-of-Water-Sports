# Импорт необходимых библиотек и классов из aiogram для создания телеграм-бота
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

# Определение токена для бота
TOKEN = "7266818477:AAEQhpIyLVS7n8h0Mc0NVb56aD65a7OxaDY"

dp = Dispatcher()

# Обработчик команды /start, который отправляет приветственное сообщение и клавиатуру с кнопками пользователю
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожалаловать, в веб-приложение, в нем вы сможете настроить свой график упражнений ')

# # Обработчик команды /hart, который отправляет сообщение и ссылку на веб-приложение myhart.ru
# @dp.message(Command('hart'))
# async def command_hart_handler(message: Message) -> None:
#     markup = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(
#                     text='Open',
#                     web_app=WebAppInfo(url=f'https://myhart.ru'),
#                 )
#             ]
#         ]
#     )
#     await message.answer('Добро пожалаловать, в веб-приложение, в нем вы сможете настроить свой график упражнений', reply_markup=markup)
    
# Обработчик всех других сообщений, который отправляет копию полученного сообщения назад в чат
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
