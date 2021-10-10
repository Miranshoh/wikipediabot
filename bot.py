import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2065372637:AAE9-ybnY45j-KQ3jt8HzlkGtsnT1av-zek'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipedia botiga Xush kelibsiz!")



@dp.message_handler()
async def sendWiki(message: types.Message):
  try:
      respond =wikipedia.summary(message.text)
      await message.reply(respond)
  except:
      await message.reply('Bu mavzuda oid maqola topilmadi')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)