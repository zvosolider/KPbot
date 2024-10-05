from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, types, F

from datetime import datetime, date

from schedule import *
from config import *

import asyncio

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

def inline(id:int):
    try:
        c = int(open("users/" + str(id)).read())
    except: c = 0
    inline_kb_list = [
        [InlineKeyboardButton(text="✅ 8 класс" if c == 8 else "8 класс", callback_data='set_8')],
        [InlineKeyboardButton(text="✅ 9 класс" if c == 9 else "9 класс", callback_data='set_9')],
        [InlineKeyboardButton(text="✅ 10 класс" if c == 10 else "10 класс", callback_data='set_10')],
        [InlineKeyboardButton(text="✅ 11 класс" if c == 11 else "11 класс", callback_data='set_11')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def days(tdate:str) -> int:
    tdobj = datetime.strptime(tdate, "%d.%m.%y")
    today = date.today()

    days = int((tdobj.date() - today).days)
    return days

def strdays(days:int) -> str:
    days %= 10
    if days == 1:
        return "день"
    elif days in [2, 3, 4]:
        return "дня"
    else:
        return "дней"


@dp.message(Command("start"))
async def start(message: types.Message, command: CommandObject):
    id = message.from_user.id
    msg = await message.answer('<b>Приветствую!</b>\nПожалуйста, выберите ваш класс:', reply_markup=inline(id))


@dp.message(Command("get_all"))
async def get_all(message: types.Message, command: CommandObject):
    id = str(message.from_user.id)
    try:
        c = int(open("users/" + id).read())
    except: await message.answer("Пожалуйста, используйте /start для определения вашего класса"); return
    string = f"<b>📚 Все АКР за {c} класс:</b>\n\n"

    if c == 8:
        for key, value in s_8.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n"
    if c == 9:
        for key, value in s_9.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n"
    if c == 10:
        for key, value in s_10.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n"
    if c == 11:
        for key, value in s_11.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n"

    await message.answer(string)


@dp.message(Command("get_month"))
async def get_all(message: types.Message, command: CommandObject):
    id = str(message.from_user.id)
    try:
        c = int(open("users/" + id).read())
    except: await message.answer("Пожалуйста, используйте /start для определения вашего класса"); return
    string = f"<b>📚 Все АКР за {c} класс на ближайший месяц:</b>\n\n"

    if c == 8:
        for key, value in s_8.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 30 else ""
    if c == 9:
        for key, value in s_9.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 30 else ""
    if c == 10:
        for key, value in s_10.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 30 else ""
    if c == 11:
        for key, value in s_11.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 30 else ""

    if string == f"<b>📚 Все АКР за {c} класс на ближайший месяц:</b>\n\n":
        string += "<i>АКР не наблюдается...</i>"

    await message.answer(string)


@dp.message(Command("get_week"))
async def get_all(message: types.Message, command: CommandObject):
    id = str(message.from_user.id)
    try:
        c = int(open("users/" + id).read())
    except: await message.answer("Пожалуйста, используйте /start для определения вашего класса"); return
    string = f"<b>📚 Все АКР за {c} класс на ближайшую неделю:</b>\n\n"

    if c == 8:
        for key, value in s_8.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 7 else ""
    if c == 9:
        for key, value in s_9.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 7 else ""
    if c == 10:
        for key, value in s_10.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 7 else ""
    if c == 11:
        for key, value in s_11.items():
            string += f"{value}: <b>{days(key)} {strdays(days(key))}</b>\n" if days(key) <= 7 else ""

    if string == f"<b>📚 Все АКР за {c} класс на ближайшую неделю:</b>\n\n":
        string += "<i>АКР не наблюдается...</i>"

    await message.answer(string)


@dp.callback_query(F.data == 'set_8')
async def set_8(call: CallbackQuery):
    with open("users/" + str(call.from_user.id), "w") as file: # ЫВАХФЫВАХФЫВАХФЫВАХФЫВ Я ТАК РЖАЛ КОГДА ЭТО ПРИДУМАЛ НО МНЕ ОЧЕНЬ ЛЕНЬ ДЕЛАТЬ ЧТО-ТО С БАЗАМИ ДАННЫХ
        file.write("8")
    await call.message.answer("✅ Ваш класс изменен на <b>восьмой</b>")
    await call.answer()


@dp.callback_query(F.data == 'set_9')
async def set_8(call: CallbackQuery):
    with open("users/" + str(call.from_user.id), "w") as file:
        file.write("9")
    await call.message.answer("✅ Ваш класс изменен на <b>девятый</b>")
    await call.answer()


@dp.callback_query(F.data == 'set_10')
async def set_8(call: CallbackQuery):
    with open("users/" + str(call.from_user.id), "w") as file:
        file.write("10")
    await call.message.answer("✅ Ваш класс изменен на <b>десятый</b>")
    await call.answer()


@dp.callback_query(F.data == 'set_11')
async def set_8(call: CallbackQuery):
    with open("users/" + str(call.from_user.id), "w") as file:
        file.write("11")
    await call.message.answer("✅ Ваш класс изменен на <b>одиннадцатый</b>")
    await call.answer()
    

async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())