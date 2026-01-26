from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telebot import types


years = [2024, 2025]
events = {2024:['конфепенция '], 2025:['турнир трёх наук']}
admin_function = ['добавить год','добавить мероприяте']

def get_year_selection_keyboard():
    year_selection_keyboard = types.InlineKeyboardMarkup()

    buttons_year =[]

    for year in years:
        buttons_year.append(types.InlineKeyboardButton(str(year), callback_data='year_'+str(year)))

    for i in buttons_year:
        year_selection_keyboard.add(i)

    return year_selection_keyboard

def get_event_selection_keyboard(year):
    event_selection_keyboard = types.InlineKeyboardMarkup()


    buttons_event = []

    for event in events[year]:
        buttons_event.append(types.InlineKeyboardButton(str(event), callback_data='event_' + str(event)))

    for i in buttons_event:
        event_selection_keyboard.add(i)

    return event_selection_keyboard

def admin_keyboard():
    admin_panel = types.InlineKeyboardMarkup()

    admin_button = []

    for function in admin_function:
        admin_button.append(types.InlineKeyboardButton(str(function), callback_data = 'admin_' + str(function)))

    for i in admin_button:
        admin_panel.add(i)

    return(admin_panel)

def add_year(year):
    years.append(year)