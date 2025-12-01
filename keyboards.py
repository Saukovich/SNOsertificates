from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types


years = [2024, 2025]
events = {}
event_2024 = ['конференция', 'турнир трёх наук']

for year in years:
    events[year] = event_2024

def get_year_selection_keyboard():
    year_selection_keyboard = types.InlineKeyboardMarkup()

    buttons_year =[]

    for year in years:
        buttons_year.append(types.InlineKeyboardButton(str(year), callback_data='year_'+str(year)))

    year_selection_keyboard.row(*buttons_year)

    return year_selection_keyboard

def get_event_selection_keyboard(year):
    event_selection_keyboard = types.InlineKeyboardMarkup()


    buttons_event = []

    for event in events[year]:
        buttons_event.append(types.InlineKeyboardButton(str(event), callback_data='event_' + str(event)))

    event_selection_keyboard.add(*buttons_event)

    return event_selection_keyboard