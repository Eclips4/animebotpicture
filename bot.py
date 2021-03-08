import logging
import requests
import asyncio
from bs4 import BeautifulSoup as bs
import random
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="1472375497:AAF1kzqYv9dSQTxZNkYET482Y6JpQVo3V0c") #1632180424:AAHiioPQ0uCxSi-p4sQ5MoHtiEc0Gsiw3Dk
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


def get_links():
    url = 'http://anime.reactor.cc/tag/Animal+Ears+%28Anime%29/best'
    mainpage = requests.get(url)
    parse_mainpage = bs(mainpage.text, 'html.parser')
    pages = parse_mainpage.find(class_='next')['href']
    pagescount = pages[pages.rfind('/') + 1:]
    art_page = requests.get(f'{url}/{random.randint(1, int(pagescount))}')
    parse_art_page = bs(art_page.text, 'html.parser')
    links_page = parse_art_page.findAll(class_="link")
    link = []
    for i in links_page:
        link.append(i['href'])
    post_link = random.choice(link)
    img_post_link = f'http://anime.reactor.cc{post_link}'
    get_post_link = requests.get(img_post_link)
    imgs = bs(get_post_link.text, 'html.parser')
    class_image = imgs.findAll(class_='image')
    list_images = []
    for i in class_image:
        my_class_image = str(i)
        link = my_class_image[
               my_class_image.find('src="') + 5:my_class_image.find(' ', my_class_image.find('src="')) - 1]
        list_images.append(link)
    for _ in list_images:
        if 'class' in str(_):
            list_images.remove(_)
    return list_images


@dp.message_handler(commands="start_send_picture")
async def send_anime(message: types.Message):
    await asyncio.sleep(1)
    while True:
        for i in get_links():
            await bot.send_photo(
                message.chat.id,
                i
            )
        await asyncio.sleep(1500)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
