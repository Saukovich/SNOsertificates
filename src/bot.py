import os
import telebot
from telebot import types
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


if __name__ == '__main__':
    bot.polling()
