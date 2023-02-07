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

user_data = ''


@dp.message_handler(commands=['start'])
async def cmd_start(message:types.Message) -> None:
    await message.answer(text='Введите число!')

@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.answer(text='Ваши данные сохранены!')

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}', parse_mode='html')

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo Bot!',
        description='Привет, я не простой ЭХО БОТ!'
    )

    await bot.answer_inline_query(results=[item],
                                inline_query_id=inline_query.id,
                                cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)