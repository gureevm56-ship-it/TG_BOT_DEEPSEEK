from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
from keyboards.command_keyboards import ButtonText, get_on_start_kb

router = Router()


class Gen(StatesGroup):
    wait = State()




@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text='Ваш запрос.',
        reply_markup=get_on_start_kb(),
    )

@router.message(F.text == ButtonText.WATS_NEXT)
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=f'Я бот-помощник.\nЗадай любой вопрос и я отвечу на него!')




@router.message(F.text == ButtonText.STOP)
@router.message(Command('stop'))
async def cmd_stop(message: Message):
    await message.answer(
        text='Если нужна помощь нажмите: /start',
        reply_markup=ReplyKeyboardRemove(),
    )



@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer(text='Подождите, запрос обрабатываестя.')



@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response)
    await state.clear()