#!/usr/bin/python

import asyncio
import os

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.environ['TEST_BOT_TOKEN'])


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет! \nЧем я могу вам помочь?'
    await bot.reply_to(message, text)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())