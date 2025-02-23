

# import telebot
# import webbrowser
# from telebot import types
# import sqlite3
#
#
# bot = telebot.TeleBot("1374966217:AAHd7GQAPMfoW8KBzKhy6tn6vzuRGioAwqQ")
# name=None
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('Abzal.Sql')
#     cur= conn.cursor()
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите свое имя ')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль ')
#     bot.register_next_step_handler(message, user_pass)
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('Abzal.Sql')
#     cur = conn.cursor()
#     cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)' ,(name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#     markup=types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Список Пользователей',callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('Abzal.Sql')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#     info = ''
#     for el in users:
#         info += f"Имя : {el[1]}, пароль : {el[2]}\n"
#     bot.send_message(call.message.chat.id, info)
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['starts'])
# def start(message):
#     markup=types.ReplyKeyboardMarkup()
#     button1=types.KeyboardButton("Перейти на сайт")   #При команде выходят варианты ответа
#     markup.add(button1)    # Первый ряд
#     button2 = types.KeyboardButton("Получить бесплатный курс Программирование на языке python с нуля")
#     markup.add(button2)
#     bot.send_message(message.chat.id,'Hello',reply_markup=markup)
#
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text=="Перейти на сайт":
#         webbrowser.open('https://google.com')
#     elif message.text=="Получить бесплатный курс Программирование на языке python с нуля":
#         file = open('./IMG_0714.JPG', 'rb')
#         bot.send_photo(message.chat.id, file,reply_markup=types.ReplyKeyboardMarkup())
#         # file = open('./Macan Asphalt 8.mp3', 'rb' )
#         # bot.send_audio(message.chat.id,file)
#
# @bot.message_handler(commands=['site','website'])
# def site(message):
#     webbrowser.open("https://kwork.ru/seller")
# @bot.message_handler(commands=['hello','Start','main'])
# def start(message):
#     bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}' )
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.reply_to(message,'Help Information: ' )
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
#     elif message.text.lower()=='id':
#         bot.reply_to(message, f"ID : {message.from_user.id}")
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup=types.InlineKeyboardMarkup()
#     button1=types.InlineKeyboardButton("Перейти на сайт", url="https://kwork.ru/seller")
#     markup.row(button1)    # Первый ряд
#     button2=types.InlineKeyboardButton("Удалить фото", callback_data='delete')
#     button3=types.InlineKeyboardButton("Изменить текст", callback_data='edit')
#     markup.row(button2,button3)    # Второй ряд
#     bot.reply_to(message,'So beautiful',reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback(call):
#     if call.data == 'delete':
#         bot.delete_message(call.message.chat.id,call.message.message_id-1)
#     elif call.data=='edit':
#         bot.send_message(call.message.chat.id,'How do you want to edit?')
#         bot.edit_message_text('edited'.text,call.message.chat.id,call.message.message_id)
# @bot.message_handler(content_types=['voice'])
# def get_voice(message):
#     bot.reply_to(message,'You are cute')
#
#
# bot.infinity_polling()



# import telebot
# import requests
# import json
# from telebot import types
#
# # Ваши токены
# BOT_TOKEN= "1374966217:AAHd7GQAPMfoW8KBzKhy6tn6vzuRGioAwqQ"
# API= "3e500c58c58559b26b47300fdf3bfd55"
#
# bot = telebot.TeleBot(BOT_TOKEN)
#
# # Команда /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(
#         message.chat.id,
#         "Привет! Я погодный бот.\n"
#         "Напиши название города, чтобы узнать текущую погоду.\n"
#         "Или воспользуйся командами:\n"
#         "/forecast [город] - прогноз на 24 часа."
#     )
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         data=json.loads(res.text)
#         temp=data["main"]["temp"]
#         cloudly=data["weather"][0]["main"]
#         bot.reply_to(message, f'Сейчас в городе {city.capitalize()} : {temp} градус Цельсия')
#         if cloudly== 'Clouds':
#             image = 'clouds.png'
#             file = open('./' + image, 'rb')
#             bot.send_photo(message.chat.id, file)
#             bot.send_message(message.chat.id, "Пасмурно")
#         elif cloudly== 'Haze' or cloudly== 'Mist':
#             image = 'mist.jpg'
#             file = open('./' + image, 'rb')
#             bot.send_photo(message.chat.id, file)
#             bot.send_message(message.chat.id, 'Туман')
#         elif cloudly== 'Clear':
#             image= 'clear.jpg'
#             file = open('./' + image, 'rb')
#             bot.send_photo(message.chat.id, file)
#             bot.send_message(message.chat.id, "Ясно")
#         elif cloudly== 'Rain':
#             image= 'rain.jpg'
#             file = open('./' + image, 'rb')
#             bot.send_photo(message.chat.id, file)
#             bot.send_message(message.chat.id, "Дождь")
#         elif cloudly== 'Snow':
#             image = 'snow.jpg'
#             file = open('./' + image, 'rb')
#             bot.send_photo(message.chat.id, file)
#             bot.send_message(message.chat.id, "Снег")
#     else:
#         bot.send_message(message.chat.id, f'Не удалось найти погоду для указанного города. Попробуйте ещё раз.')
# bot.infinity_polling()
# from currency_converter import CurrencyConverter
# C= CurrencyConverter()
# import telebot
# from telebot import types
# bot = telebot.TeleBot("1374966217:AAHd7GQAPMfoW8KBzKhy6tn6vzuRGioAwqQ")
# amount = 0
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, введите сумму для конвертации.')
#     bot.register_next_step_handler(message, summa)
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Не верный формат, попробуйте еще раз.')
#         return
#     if amount >0:
#         markup=types.InlineKeyboardMarkup(row_width=2)
#         btn1=types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP')
#         btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Сумма должна быть больше 0, попробуйте еще раз.')
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data!='else':
#         values=call.data.split('/')
#         res=C.convert(amount,values[0],values[1])
#         bot.send_message(call.message.chat.id, f'Получается {round(res,2)}, можете еще раз ввести сумму')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, "Введите две валюты через /")
#         bot.register_next_step_handler(call.message, mycur)
# def mycur(message):
#     try:
#         values = message.text.upper().split('/')
#         res = C.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается {round(res, 2)}, можете еще раз ввести сумму')
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, 'Не верный формат, попробуйте еще раз.')
#         bot.register_next_step_handler(message, mycur)
#         return
#
#
#
# bot.infinity_polling()

from fastapi import FastAPI, Request
import asyncio
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
import logging
from database.handlers import router
from aiogram import Bot, Dispatcher
from database.models import async_main
from aiogram.types import Update
env_path = r"C:\Users\Almaz\PycharmProjects\PythonProject3\.venv\.env"
load_dotenv(env_path)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()  # Создаём объект Dispatcher без bot
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Бот запущен!")  # Здесь можешь добавить логику старта бота
    yield
    print("Бот выключается...")  # Это выполнится при завершении работы

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    return {"message": "Бот работает!"}

dp.include_router(router)

async def main():
    await async_main()
    await bot.delete_webhook()
    await dp.start_polling(bot)  # Передаем bot в start_polling

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
