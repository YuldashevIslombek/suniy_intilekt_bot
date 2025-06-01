import asyncio
import logging
from http.client import responses
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from deepsek import generate_response

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
AI_TOKEN = getenv("AI_TOKEN")
dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("privet")

@dp.message()
async def echo(message: Message) -> None:
    response = await generate_response(message.text, AI_TOKEN)
    await message.answer(f"{response}", html=True)


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    asyncio.run(main())
