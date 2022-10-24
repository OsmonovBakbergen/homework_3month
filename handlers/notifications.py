import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('OK!')


async def go_to_lesson():
    await bot.send_message(chat_id=chat_id, text='Сегодня урок в гиктеке!')


async def scheduler():
    aioschedule.every().wednesday.at('7:30').do(go_to_lesson)
    aioschedule.every().saturday.at('7:30').do(go_to_lesson)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)