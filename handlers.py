from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb


router = Router()





@router.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer_sticker('CAACAgIAAxkBAAEL8npmIW5tVf_A2HOIXh7e9dPVeSTYgwACVzIAAlZfGEuQ00oChUPYQzQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8nxmIW5xuuIVlSg1jbSReusrur94PQACKiUAAua_GUtodTWTfplsujQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8n5mIW5zwuVvP-4Gbt3dOCMmSJl4eAACuS8AAgS3EEuL1jlbFPjxTTQE')
   await message.answer(f'Привет,{message.from_user.first_name}, я бот который будет давать ссылку на аниме!',
                        reply_markup=kb.main)