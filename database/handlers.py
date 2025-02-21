import telebot
import webbrowser
from aiofiles.os import replace
from aiogram import  F, Router
from aiogram.types import Message, callback_query
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import database.keyboards as kb
import database.models as md
from openai import AsyncOpenAI
from database.generators import gpt4
import database.requests as rq
from telebot import states
from database.middlewares import TestMiddleware
import openai
router = Router()
import markdown
import re
router.message.middleware(TestMiddleware())
class Reg(StatesGroup):
    name = State()
    number = State()

# @router.message(CommandStart())
# async def cmd(message: Message):
#     await message.answer('Hello')

# @router.message(F.text =='Как дела')
# async def hru(message: Message):
#     await message.answer('OK')
#
# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#      await message.answer_photo(
#      #photo = 'AgACAgIAAxkBAAIExWeWVXGJm26xn_DGuDHFr5N3jA8OAALW9DEbg_qwSK7DbeCTSg17AQADAgADeQADNgQ'
#      photo='https://img.freepik.com/premium-photo/cloudy-blue-sky-beautiful-sky-clouds_692702-1814.jpg?w=740',
#      caption= 'This is cloudy sky!')
# @router.message(F.photo)
# async def photo(message: Message):
#     await message.answer("So beautiful")
#     await message.answer(f'ID фото {message.photo[-1].file_id}')
# @router.callback_query(F.data =='catalog')
# async def cat(callback : callback_query):
#     await callback.answer('Вы выбрали каталог')
#     await callback.message.edit_text('Привет', reply_markup=await kb.inline_cars())
#
#
# @router.message(Command('Register'))
# async def reg1(message: Message, state : FSMContext ):
#     await state.set_state(Reg.name)
#     await message.answer("Введите ваше имя ")
#
# @router.message(Reg.name)
# async def reg2(message: Message, state : FSMContext ):
#     await state.update_data(name=message.text)
#     await state.set_state(Reg.number)
#     await message.answer("Введите номер телефона без  '+' ")
# @router.message(Reg.number)
# async def reg3(message: Message, state : FSMContext ):
#     await state.update_data(number=message.text)
#     data= await state.get_data()
#     await message.answer(f"Вы успешно зарегистрировались в базу данных ! \nИмя пользователя : {data['name']}  \nНомер телефона : {data['number']}")
#     await state.clear()

#______________________________________________________________________

# @router.message(Command('start', 'Start', 'старт'))
# async def start(message: Message):
#     await rq.set_user(message.from_user.id)
#     await message.answer(f'Hello , {message.from_user.first_name}! ',
#                         # reply_markup=kb.main,
#                         # reply_markup=kb.settings,
#                         # reply_markup= await kb.inline_cars())
#                           reply_markup=kb.menu)


# @router.message(F.text=="Каталог")
# async def start(message: Message):
#     await message.answer("Выберите категорию товара", reply_markup= await kb.categories())
# @router.callback_query(F.data.startswith('category_'))
# async def category_start(callback: callback_query, state: FSMContext):
#     await callback.answer("Вы выбрали категорию")
#     await callback.message.answer("Выберите товар по категории",
#                                   reply_markup=await kb.items(callback.data.split("_")[1]))
# @router.callback_query(F.data.startswith('item_'))
# async def item_start(callback: callback_query, state: FSMContext):
#     item_data = await rq.get_item(callback.data.split("_")[1])
#     await callback.answer("Вы выбрали товар")
#     await callback.message.answer(f"Название : {item_data.name}\nОписание : {item_data.description}\nЦена : {item_data.price}",
#                                   reply_markup= kb.basketk)
#     await state.update_data(item_name=item_data.name)
# @router.callback_query(F.data=='basketk')
# async def basketk(callback: callback_query, state: FSMContext):
#     data = await state.get_data()
#     item_name = data.get("item_name")
#     await callback.answer('Вы добавили товар в корзину',reply_markup = kb.basketk1)
#     md.basket.append(item_name)
# @router.callback_query(F.data=='to main')
# async def main(callback: callback_query, state: FSMContext):
#     await callback.answer('', reply_markup= kb.menu)
# @router.message(F.text=="Корзина")
# async def start(message: Message):
#     if md.basket == None:
#         await message.answer("Ваша корзина пуста")
#     else:
#         await message.answer(f"В вашей корзине находятся {md.basket[0]}")

#______________________________________________________________________________________
class Generate(StatesGroup):
    text = State()
context_memory = {}
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if message.from_user.username == "Erhandro":
        await message.answer("Добро пожаловать, Чучмек! Введите свой запрос, только не связаный с фашизмом")
    else:
        await message.answer("Добро Пожаловать! Введите Ваш запрос")

        await state.clear()

@router.message(Command("help"))
async def lowkrt(message: Message):
    await message.answer("В какой помощи ты нуждаешься?")
@router.message(Command("site"))
async def site(message:Message):
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")


def markdown_to_html(text: str) -> str:
    if not isinstance(text, str):
        return ""

    # Заменяем **жирный** на <b>жирный</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    # Заменяем *курсив* и _курсив_ на <i>курсив</i>
    text = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)  # Для *курсив*
    text = re.sub(r'(?<!_)_(?!_)(.*?)(?<!_)_(?!_)', r'<i>\1</i>', text)  # Для _курсив_

    return text

@router.message(F.text)
async def hane(message: Message, state: FSMContext):
    user_id = message.chat.id
    user_message = message.text

    # Загружаем контекст пользователя
    if user_id not in context_memory:
        context_memory[user_id] = []

    # Добавляем новое сообщение в историю
    context_memory[user_id].append({"role": "user", "content": user_message})

    # Ограничиваем историю (например, 10 последних сообщений)
    context_memory[user_id] = context_memory[user_id][-10:]

    await state.set_state(Generate.text)

    response = gpt4(context_memory[user_id])
    if not response:
        await message.answer("Произошла ошибка при генерации ответа.")
        return
    content = response.choices[0].message.content
    context_memory[user_id].append({"role": "assistant", "content": content})
    if not isinstance(content, str):
        content = "Ошибка: пустой ответ от ИИ"

    html = markdown_to_html(content)

    await message.answer(html, parse_mode="HTML")  # Исправлено "html" -> "HTML"

    await state.clear()


@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer('Подождите, Ваш ответ генерируется...')

