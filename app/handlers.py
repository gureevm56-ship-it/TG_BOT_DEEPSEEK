import sys

from aiogram import Bot
from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from app.generate import ai_generate
from keyboards.command_keyboards import ButtonText, get_on_start_kb


from config import TG_TOKEN





router = Router()

bot = Bot(token=TG_TOKEN)

class Gen(StatesGroup):
    wait = State()


#Команда "старт" начало бота

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text='Ваш запрос.',
        reply_markup=get_on_start_kb(),
    )


#Узнать что делает бот

@router.message(F.text == ButtonText.WATS_NEXT)
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=f'Я бот-помощник.\nЗадай любой вопрос и я отвечу на него!')



#Команда "стоп" - остановить бота

@router.message(F.text == ButtonText.STOP)
@router.message(Command('stop'))
async def cmd_stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text='Если нужна помощь нажмите: /start',
        reply_markup=ReplyKeyboardRemove()
    )
    sys.exit(0)


#Задать вопрос нейросети

@router.message(F.text == ButtonText.QUESTION)
@router.message(Command('ask'))
async def ask_start(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    await message.answer('Задайте ваш вопрос нейросети.')


#Анти-спам
@router.message(Gen.wait)
async def generating(message: Message, state: FSMContext):
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()
