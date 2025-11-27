from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_year_selection_keyboard():
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton("Кнопка 1", callback_data="1")
    )

    return markup