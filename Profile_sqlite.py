from aiogram import types, executor, Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from sqlite import db_start, create_profile, edit_profile

async def on_startup(_):
    await db_start()


storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,storage=storage)

class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    desc = State()

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))

    return kb

def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/cancel'))

    return kb

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Добро пожаловать! Чтобы начать создавать твой профиль нажми на кнопку "/create"', reply_markup=get_kb())
    await create_profile(user_id=msg.from_user.id)

@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.reply('Вы прервали создание профиля!', reply_markup=get_kb())

@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.reply('Давай создадим твой профиль! Отправь мне свое фото!', reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()

@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('Это не фото!')

@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await message.reply('Теперь отправь свое имя!')
    await ProfileStatesGroup.next()

@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100, state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply('Введите реальный возраст')

@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply('Сколько тебе лет?')
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text
    await message.reply('Теперь расскажи немного о себе!')
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.desc)
async def load_desc(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['desc'] = message.text
        await bot.send_photo(chat_id=message.from_user.id, 
                            photo=data['photo'], 
                            caption=f"{data['name']}, {data['age']}\n{data['desc']}")
    await edit_profile(state, user_id=message.from_user.id)
    await message.answer('Ваша анкета успешно создана')
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)