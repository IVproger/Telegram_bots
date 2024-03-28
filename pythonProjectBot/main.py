from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import emoji



bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

# bot logic
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(emoji.emojize(f'{message.from_user.first_name}, приятно познакомиться :beaming_face_with_smiling_eyes:'))
    await message.answer('Я Бот, твой персональный помощник и верный друг. Напиши команду /help, чтобы узнать что я умею.')

@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("Я пока только учусь. Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


# bot initialising
if __name__ == '__main__':
    executor.start_polling(dp)