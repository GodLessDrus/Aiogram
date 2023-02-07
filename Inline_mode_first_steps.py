from aiogram import types, executor, Dispatcher,Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API
import random
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import asyncio
import hashlib

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
cb = CallbackData('ikb', 'action')

def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton('Button 1', callback_data=cb.new('first'))],
                                [InlineKeyboardButton('Button 2', callback_data=cb.new('second'))]
    ])

    return ikb

@dp.message_handler(commands=['start'])
async def cmd_start(message:types.Message) -> None:
    await message.answer(text='Ну здарова!', reply_markup=get_ikb())

@dp.callback_query_handler(cb.filter(action='first'))
async def first_cb(callback: types.CallbackQuery) -> None:
    await callback.answer('Hello!')

@dp.callback_query_handler(cb.filter(action='second'))
async def second_cb(callback: types.CallbackQuery) -> None:
    await callback.answer('World!')

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo' #получили текст от пользователя
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest() #сделали уникальный id результата

    if text == 'photo':
        input_content = InputTextMessageContent('This is a photo')

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title=text
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                results=[item])




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)