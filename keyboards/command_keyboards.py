from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = 'Hello!'
    WATS_NEXT = "What's next?"
    STOP = 'Stop'


def get_on_start_kb():
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WATS_NEXT)
    button_stop = KeyboardButton(text=ButtonText.STOP)
    buttons_first_row = [button_hello, button_help]
    buttons_second_row = [button_stop]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


    return markup
