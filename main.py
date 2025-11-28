#!/usr/bin/python

import asyncio
import os

from telebot.async_telebot import AsyncTeleBot
from keyboards import *
from messages import *

bot = AsyncTeleBot(os.environ['TEST_BOT_TOKEN'])


# Handle '/start' and '/help'
@bot.message_handler(commands='start')
async def send_welcome(message):
    """
    Отвечает на сообщение /start

    :param message: сообщение, на которое отвечает бот
    :return: None
    """
    text = start_message
    year_selection_keyboard = get_year_selection_keyboard()
    await bot.reply_to(message, text, reply_markup=year_selection_keyboard)

@bot.callback_query_handler(func=lambda call:call.data.startswith('year_'))
async def handle_year (call):
    """
        Позволяет выбрать мероприятие в выбранном году

        :return: None
    """
    year = call.data.replace('year_', '')
    text = change_event_message + year +'-го года'
    event_selection_keyboard = get_event_selection_keyboard()
    await bot.send_message(call.message.chat.id, text, reply_markup=event_selection_keyboard)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_unknown_message(message):
    """
    Отвечает на неопознанные сообщения

    :param message: сообщение, на которое отвечает бот
    :return: None
    """
    text = unknown_message
    await bot.reply_to(message, text)

if __name__ == '__main__':
    asyncio.run(bot.polling())