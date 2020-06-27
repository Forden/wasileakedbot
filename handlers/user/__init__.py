from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from .check import check
from .start import bot_start
from .stats import get_stats


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(get_stats, commands=['stats'], is_admin=True)

    dp.register_message_handler(check)
