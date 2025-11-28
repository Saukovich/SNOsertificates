from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types

def get_year_selection_keyboard():
    year_selection_keyboard = types.InlineKeyboardMarkup()

    years = [2024, 2025]
    buttons =[]

    for year in years:
        buttons.append(types.InlineKeyboardButton(str(year), callback_data='year_'+str(year)))

    year_selection_keyboard.row(*buttons)

    return year_selection_keyboard

def get_event_selection_keyboard():
    event_selection_keyboard = InlineKeyboardMarkup()

    event_selection_keyboard.row(
    InlineKeyboardButton("конференция", callback_data="event_conf")
    )

    return event_selection_keyboard