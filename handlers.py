from aiogram import types, F, Router
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder

import random
import config
import kb, db
import text

router = Router()
bot = Bot(token=config.BOT_TOKEN)

class Form(StatesGroup):
    menu = State()

@router.message(F.text == "Старт")
@router.message(F.text == "Начать")
@router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=text.start, reply_markup=kb.menu)

@router.message(Command("help"))
async def help(message: Message):
    await message.answer(text.help, reply_markup=kb.back_to_menu)

@router.message(Command("exit"))
async def exit(state: FSMContext):
    await state.menu()

@router.callback_query(F.data == "menu")
async def menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text.menu, reply_markup=kb.menu)

#Админка

@router.callback_query(F.data == "admin_back")
async def menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.message.from_user.username in config.admin_list:
        await callback_query.message.edit_text(text.admin, reply_markup=kb.admin)
    else:
        await callback_query.message.edit_text('Ошибка: Вы не являетесь администратором', reply_markup=kb.back_to_menu)

@router.message(Command("admin"))
async def help(message: Message):
    if message.from_user.username in config.admin_list:
        await message.edit_text(text.admin, reply_markup=kb.admin)
    else:
        await message.edit_text('Ошибка: Вы не являетесь администратором', reply_markup=kb.back_to_menu)

@router.callback_query(F.data == "admin_menu1")
async def help(message: Message, callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if message.from_user.username in config.admin_list:
        await message.edit_text(text.load_post, reply_markup=kb.load_post)
    else:
        await message.answer('Ошибка: Вы не являетесь администратором', reply_markup=kb.back_to_menu)



#vvvvv

@router.callback_query(F.data == "categories")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text.cat, reply_markup=kb.back_to_menu)

@router.callback_query(F.data == "cabinet")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text.cab, reply_markup=kb.back_to_menu)

@router.callback_query(F.data == "support")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text.support, reply_markup=kb.back_to_menu)

@router.callback_query(F.data == "faq")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text.faq, reply_markup=kb.back_to_menu)
