from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
import random


from config import TOKEN_API
from keyboards import kb, kb1, kb_pic,ibtp


bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание бота</em>
<b>/picture</b> - <em>картинка котика</em>
<b>/mult</b> - <em>сайты с мультиками</em>
"""

KitPic = ['https://i.pinimg.com/736x/f4/d2/96/f4d2961b652880be432fb9580891ed62.jpg',
         'https://cdnn21.img.ria.ru/images/148839/96/1488399659_0:0:960:960_600x0_80_0_1_e38b72053fffa5d3d7e82d2fe116f0b3.jpg', 
         'https://cs11.pikabu.ru/post_img/2019/02/04/12/1549312329147951618.jpg',
         'https://oir.mobi/uploads/posts/2021-04/1619619348_59-oir_mobi-p-samie-milie-kotiki-zhivotnie-krasivo-foto-65.jpg',
         'https://klike.net/uploads/posts/2018-10/1539499416_1.jpg', 
         'https://fatcatart.com/wp-content/uploads/2021/03/pussy-willow-cats-v-w.jpg',
         'https://koshka.top/uploads/posts/2021-12/1639885690_1-koshka-top-p-mini-kotiki-1.jpg',
         'https://oir.mobi/uploads/posts/2021-05/1621032934_9-oir_mobi-p-mimishnie-kotiki-zhivotnie-krasivo-foto-10.jpg', 
         'https://rg.ru/uploads/images/178/22/40/kotik.jpg',
         'https://i.pinimg.com/736x/90/5f/b9/905fb99eef0b84006bab98f379739a51.jpg',
         'https://koshka.top/uploads/posts/2021-12/1640199637_1-koshka-top-p-milie-kotiki-v-odezhde-1.jpg', 
         'https://kartinkof.club/uploads/posts/2022-05/1653640320_1-kartinkof-club-p-veselie-kotiki-kartinki-1.jpg',
         'https://happypik.ru/wp-content/uploads/2019/09/njashnye-kotiki20.jpg',
         'https://phonoteka.org/uploads/posts/2021-06/1624296425_34-phonoteka_org-p-oboi-na-rabochii-stol-kotiki-krasivo-35.jpg', 
         'https://cs11.pikabu.ru/post_img/big/2020/02/19/12/1582144929123946147.jpg',
         'https://vn.ru/upload/iblock/540/54023de5_c1d36e32fff7556eae4fbe03_thumb_729-486_ea44ecca0b594017-ae361.jpg',
         'https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg', 
         'https://oir.mobi/uploads/posts/2021-04/1619714866_25-oir_mobi-p-milenkie-kotiki-zhivotnie-krasivo-foto-29.jpg',
         'https://zefirka.net/wp-content/uploads/2022/06/milye-kotiki-zaryazhayut-pozitivom-na-snimkax-1.jpg',
         'https://humor.fm/upload/post/2019/10/22/1721288/kotiki-12.jpg', 
         'https://i.pinimg.com/736x/7d/7e/62/7d7e62c7cc37b18f7002e93dded59853.jpg',
         'https://gamerwall.pro/uploads/posts/2022-09/1662413500_1-gamerwall-pro-p-krutie-kotiki-krasivo-1.jpg',
         'https://sites.google.com/site/kotiki14356677/_/rsrc/1400132482540/home/%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8.jpg', 
         'https://oir.mobi/uploads/posts/2021-04/1619736998_1-oir_mobi-p-milie-kotiki-oboi-zhivotnie-krasivo-foto-1.jpg',
         'https://phonoteka.org/uploads/posts/2021-06/1624728823_14-phonoteka_org-p-smeshnie-kotiki-oboi-krasivo-21.jpg',
         'https://img.myslo.ru/Photogallery/97/da/97dad590-b258-4fe1-91e7-47c29a833d01_s3.jpg', 
         'https://i.pinimg.com/736x/b9/bf/07/b9bf0781e95f66e632d3a5464afbfb23.jpg',
         'http://giffun.ru/wp-content/uploads/2019/04/Kartinki_nyashnye_kotiki_1_25043556.jpg',
         'https://medialeaks.ru/wp-content/uploads/2019/07/3-5d2cd2b17bdca__880-1-500x500.jpg', 
         'https://www.meme-arsenal.com/memes/3aa1ad78808ae13a5656e22cc9d758e5.jpg',
         'https://n1s1.hsmedia.ru/f2/e3/9c/f2e39cb1817739d34f20f5da82442807/728x728_1_562f6b23003fe3bee9b459aa8a538126@1080x1080_0xac120003_17745537941663941356.jpeg',
         'https://omoro.ru/wp-content/uploads/2019/08/prikolnye-kotiki-2.jpg', 
         'https://phonoteka.org/uploads/posts/2022-06/thumbs/1654154577_2-phonoteka-org-p-kotiki-oboi-na-rabochii-stol-krasivo-3.jpg',
         'https://oir.mobi/uploads/posts/2021-05/1620939233_7-oir_mobi-p-kotiki-nyashki-zhivotnie-krasivo-foto-7.jpg',
         'https://www.m24.ru/b/d/nBkSUhL2gVMkn8-0PqzJrMCqzJ3w-pun2XyQ2q2C_2OZcGuaSnvVjCdg4M4S7FjDvM_AtC_QbIk8W7zj1GdwKSGT_w=NWGtprpGA6b7Cy2657h8rw.jpg', 
         'https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628822406_89-p-zabavnie-kotiki-foto-92.jpg',
         'https://medialeaks.ru/wp-content/uploads/2017/10/catbread-03-600x400.jpg',
         'https://trikky.ru/wp-content/blogs.dir/1/files/2020/04/22/1564314090_3.jpg', 
         'https://img-fotki.yandex.ru/get/6808/200606445.36/0_128218_d5cb734_XL.jpg',
         'http://www.k1.ua/uploads/news_channel/2015/01/20/ccfc0e0f3d16d64c52991e4e4f02687496bb77f7.jpg',
         'https://cdn-irec.r-99.com/sites/default/files/imagecache/copyright/user-images/13405/emoNxJGJ3NydM0LQ1tkxSQ.jpg', 
         'https://static2.tgstat.ru/channels/_0/e4/e4d0807d7a8839e09433a12884e33c15.jpg']

photos = dict(zip(KitPic, ['1 рандомное фото котика из 42',
                        '2 рандомное фото котика из 42',
                        '3 рандомное фото котика из 42',
                        '4 рандомное фото котика из 42',
                        '5 рандомное фото котика из 42',
                        '6 рандомное фото котика из 42',
                        '7 рандомное фото котика из 42',
                        '8 рандомное фото котика из 42',
                        '9 рандомное фото котика из 42',
                        '10 рандомное фото котика из 42',
                        '11 рандомное фото котика из 42',
                        '12 рандомное фото котика из 42',
                        '13 рандомное фото котика из 42',
                        '14 рандомное фото котика из 42',
                        '15 рандомное фото котика из 42',
                        '16 рандомное фото котика из 42',
                        '17 рандомное фото котика из 42',
                        '18 рандомное фото котика из 42',
                        '19 рандомное фото котика из 42',
                        '20 рандомное фото котика из 42',
                        '21 рандомное фото котика из 42',
                        '22 рандомное фото котика из 42',
                        '23 рандомное фото котика из 42',
                        '24 рандомное фото котика из 42',
                        '25 рандомное фото котика из 42',
                        '26 рандомное фото котика из 42',
                        '27 рандомное фото котика из 42',
                        '28 рандомное фото котика из 42',
                        '29 рандомное фото котика из 42',
                        '30 рандомное фото котика из 42',
                        '31 рандомное фото котика из 42',
                        '32 рандомное фото котика из 42',
                        '33 рандомное фото котика из 42',
                        '34 рандомное фото котика из 42',
                        '35 рандомное фото котика из 42',
                        '36 рандомное фото котика из 42',
                        '37 рандомное фото котика из 42',
                        '38 рандомное фото котика из 42',
                        '39 рандомное фото котика из 42',
                        '40 рандомное фото котика из 42',
                        '41 рандомное фото котика из 42',
                        '42 рандомное фото котика из 42']))
random_photo = random.choice(list(photos.keys()))


flag = False

async def on_startup(_):
    print('Я запустился!')

async def send_random(message: types.message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id, photo=random_photo, caption=photos[random_photo], reply_markup=ibtp)
    


@dp.message_handler(Text(equals='picture'))
async def open_kb_pic(message: types.message):
    await message.answer(text='Рандомный котик!', reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb_pic(message: types.message):
    await message.answer(text='Вы вернулись в главное меню!', reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['start'])
async def command_start(message:types.message):
    await bot.send_message(chat_id=message.from_user.id, text='<em>Для получения помощи введи команду /help</em>',parse_mode="HTML",
                        reply_markup=kb1)

@dp.message_handler(commands=['help'])
async def command_help(message:types.message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND,parse_mode="HTML", reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def command_description(message:types.message):
    await bot.send_message(chat_id=message.from_user.id, text='<em>Этот бот самый простой и пока ничего не может</em>', parse_mode="HTML", reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['mult'])
async def command_mult(message:types.message):
    ibt = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Griffins', url='https://serial-time.com/217-griffiny-9-sezon-s9.html', callback_data='grif')
    ib2 = InlineKeyboardButton(text='South Park', url='https://www.southparkfan.ru/sezon/sp.see.online.php?s=aa2', callback_data='south')
    ib3 = InlineKeyboardButton(text='Не интересно!', callback_data='not_intresting')
    ibt.add(ib2, ib1, ib3)
    await bot.send_photo(chat_id=message.from_user.id, photo='https://cs.pikabu.ru/post_img/2013/05/15/10/1368636743_42044010.jpg',caption= 'Вот две кнопки на достаточно интересные мультики!', reply_markup=ibt)
    await message.delete()


@dp.callback_query_handler()
async def mess_callback(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'not_intresting':
            await callback.answer(text='Очень жаль, что тебе не понравились эти мультики')
    elif callback.data == 'like':
        if not flag:
            await callback.answer('Вам понравился этот котик!')
            flag = not flag
        else:
            await callback.answer(text='Вы уже лайкали')
    elif callback.data == 'dislike':
            await callback.answer(text='Вам не понравился этот котик!')
    elif callback.data == 'main':
        await callback.message.answer(text='Возвращаемся в главное меню!', reply_markup=kb)
        await callback.answer()
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo, type='photo', caption=photos[random_photo]),reply_markup=ibtp)
        await callback.answer()
    


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True, on_startup=on_startup)