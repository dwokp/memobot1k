import os
import random

import praw
from aiogram import Bot, Dispatcher, types
import asyncio
from PIL import Image, ImageDraw, ImageFont
import asyncio

from aiogram.filters import Command

# Настройки API
API_TOKEN = "7826898830:AAFsuB8JkLGRONunmNLN1_aIM6WBApZyBNM"
REDDIT_CLIENT_ID = "I3hFYOwbEDquQr_zJ9Q55A"
REDDIT_SECRET = "ZKTjcO38kibcLarjKMu4OKs8_Ynw-g"
REDDIT_USER_AGENT = "@memograaam_bot"

# Инициализация бота и Reddit API
bot = Bot(token=API_TOKEN)
dp = Dispatcher(Bot=bot)

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT)


# Команда для отправки мемов из Reddit
dp = Dispatcher()
@dp.message(Command("meme"))
async def send_meme(message: types.Message):
    subreddit = reddit.subreddit("memes")
    posts = [post for post in subreddit.hot(limit=50)]
    meme = random.choice(posts)

    if meme.url.endswith(("jpg", "png", "jpeg")):
        await bot.send_photo(message.chat.id, meme.url, caption=meme.title)
    else:
        await message.reply("Не удалось найти подходящий мем.")


# Команда для отправки локальных мемов
@dp.message(Command("local_meme"))
async def send_local_meme(message: types.Message):
    meme_folder = "memes/"
    meme_files = os.listdir(meme_folder)

    if not meme_files:
        await message.reply("В папке с мемами нет файлов.")
        return

    meme_path = os.path.join(meme_folder, random.choice(meme_files))

    with open(meme_path, "rb") as meme:
        await bot.send_photo(message.chat.id, meme)


# Функция для генерации мемов с текстом
def generate_meme(text_top, text_bottom):
    image_path = random.choice(os.listdir("memes/"))
    img = Image.open(f"memes/{image_path}")
    draw = ImageDraw.Draw(img)

    # Убедитесь, что шрифт доступен
    try:
        font = ImageFont.truetype("impact.ttf", 50)
    except IOError:
        font = ImageFont.load_default()  # Используйте шрифт по умолчанию, если impact.ttf недоступен

    # Добавление текста на изображение
    draw.text((10, 10), text_top, font=font, fill="white")
    draw.text((10, img.height - 60), text_bottom, font=font, fill="white")

    # Сохранение сгенерированного мема
    output_path = "generated_meme.jpg"
    img.save(output_path)
    return output_path


# Команда для генерации мемов
@dp.message(Command("generate_meme"))
async def create_meme(message: types.Message):
    # Пример текста для мема
    text_top = "Верхний текст"
    text_bottom = "Нижний текст"

    meme_path = generate_meme(text_top, text_bottom)

    with open(meme_path, "rb") as meme:
        await bot.send_photo(message.chat.id, meme)


# Запуск бота
async def main():
    await dp.start_polling(bot)

if 'name' == "main":
    asyncio.run(main())
