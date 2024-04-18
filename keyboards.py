from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Получить')],
    [KeyboardButton(text='Зарегистрироваться'), KeyboardButton(text='Удалить аккаунт')]
],                                                             

                                resize_keyboard= True,
                                input_field_placeholder = 'Нажми кнопку милый')











