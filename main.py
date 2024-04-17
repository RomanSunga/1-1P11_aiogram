import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN


bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('https://ya.ru/images/search?family=yes&img_url=https%3A%2F%2Fi.artfile.me%2Fwallpaper%2F13-03-2016%2F3191x2250%2Fanime-unknown--drugoe-niya-tidsean-1017532.jpg&lr=7&nl=1&p=1&pos=33&rpt=simage&source=morda&text=Аниме%20Арты')




async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')