import sys
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate




router = Router()


class Gen(StatesGroup):
    wait = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Ваш запрос.')


@router.message(Command('stop'))
async def cmd_stop(message: Message):
    sys.exit(0)

@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer('Подождите, запрос обрабатываестя.')



@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()