from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_start_router = Router()


@user_start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.reply(f"Hello, {message.from_user.full_name}!")
