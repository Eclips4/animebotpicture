import logging
import asyncio
from get_picture import Picture
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="ENTER_YOUR_TOKEN")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start_send_picture")
async def send_anime(message: types.Message):
    await asyncio.sleep(1)
    while True:
        try:
            for i in Picture('http://anime.reactor.cc/tag/Animal+Ears+%28Anime%29/best').get_pictures():
                await bot.send_photo(
                    message.chat.id,
                    i
                )
                print('send', i)
            await asyncio.sleep(100)
        except:
            await asyncio.sleep(1)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
