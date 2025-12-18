from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = 'Hello!'
    WATS_NEXT = "About"
    STOP = 'Stop'
    QUESTION = 'Question'



#Кнопки вместо клавиатуры в тг
def get_on_start_kb():
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WATS_NEXT)
    button_stop = KeyboardButton(text=ButtonText.STOP)
    button_question = KeyboardButton(text=ButtonText.QUESTION)
    buttons_first_row = [button_hello, button_help]
    buttons_second_row = [button_stop, button_question]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


    return markup
