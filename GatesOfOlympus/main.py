import asyncio
import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, Message
from data.UserRepository import UserRepository
from config import *


dp = Dispatcher()


def kb_menu(url):
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Play", web_app=WebAppInfo(url=url))]
    ])


@dp.message(Command("start"))
async def start(message: Message):
    user = UserRepository().get_user(message.from_user.id)
    if not user:
        return  # organic

    await message.answer("Hello", reply_markup=kb_menu(user['url']))


async def run_bot():
    logging.basicConfig(level=logging.INFO)
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=BOT_TOKEN, default=default_properties)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start (tg web app) bot: {e}")


if __name__ == '__main__':
    asyncio.run(run_bot())
