from aiogram import types, executor, Dispatcher,Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API
import random
from aiogram.utils.callback_data import CallbackData

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton('Button', callback_data=cb.new('push'))]
])





@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hello', reply_markup=ikb)

@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('Something!')



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)