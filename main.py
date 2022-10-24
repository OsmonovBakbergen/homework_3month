import asyncio

from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import callback, admin, fsm_mentor, exstra, client, notifications
from Database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


notifications.register_handlers_notification(dp)
fsm_mentor.register_handlers_fsm(dp)
admin.register_handlers_ADMIN(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
exstra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
