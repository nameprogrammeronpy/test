from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from database.requests import get_categories, get_category_item

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],   # Первый ряд
#     [KeyboardButton(text='Корзина'),KeyboardButton(text='Контакты')]   # Второй ряд
#      ],
#     resize_keyboard=True, input_field_placeholder='Выберите пункт')
# settings = InlineKeyboardMarkup(inline_keyboard=[
# [InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/watch?v=qRyshRUA0xM&t=181s')]
#
# ])

# menu = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог',callback_data='catalog')],
#     [InlineKeyboardButton(text='Корзина' callback_data='basket')],
#     [InlineKeyboardButton(text='Контакты' callback_data='contacts')]])
basketk1= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти в корзину', callback_data='basketk1')],
[InlineKeyboardButton(text='На главную', callback_data='to main')]])
basketk = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить в корзину', callback_data='basketk')],
[InlineKeyboardButton(text='На главную', callback_data='to main')]


])
menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')]],
resize_keyboard=True, input_field_placeholder='Выберите пункт...')
async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to main'))
    return keyboard.adjust(2).as_markup()
async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to main'))
    return keyboard.adjust(2).as_markup()

# cars= ['Mercedes', 'BMW', 'Tesla', 'Toyota', 'Lexus', 'Nexia', 'Chevrole','Bugatti']
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
#     return keyboard.adjust(4).as_markup()