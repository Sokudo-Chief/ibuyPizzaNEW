import logging
from aiogram import executor
from create_bot import dp
from handlers import client, zakaz_burgeri, zakaz_bulochki

logging.basicConfig(level=logging.INFO)


zakaz_bulochki.register_handlers(dp)
zakaz_burgeri.register_handlers(dp)
client.register_handlers(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
