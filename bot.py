import asyncio
import logging
import os
import re
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = BOT_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
YOUTUBE_URL_REGEX = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+"
TIKTOK_URL_REGEX = r"(https?://)?(www\.)?(tiktok)\.(com)/.+"

@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer("Send Me A YouTube Or TikTok Link")

@dp.message()
async def handle_video_download(message: types.Message):
    url = message.text
    chat_id = message.chat.id
    logger.info(f"Received URL: {url}")

    if not re.match(YOUTUBE_URL_REGEX, url) and not re.match(TIKTOK_URL_REGEX, url):
        logger.info("URL does not match regex")
        await message.answer("This Link Is Not Correct")
        return

    send_message = await message.reply("Download Started, Please Wait")
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(id)s.%(ext)s',
            'noplaylist': True,
            'nooverwrites': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info_dict)
            logger.info(f"Downloaded video: {video_file}")

        if os.path.exists(video_file):
            await send_message.edit_text("Video Has Been Downloaded. Sending Now...")
            video_to_send = FSInputFile(video_file)
            await bot.send_video(chat_id, video_to_send)
        else:
            logger.error(f"File not found: {video_file}")
            await send_message.edit_text(f"File not found: {video_file}")

    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Download error: {e}")
        await send_message.edit_text(f"Download error: {e}")
    except Exception as exp:
        logger.error(f"Unexpected error: {exp}")
        await send_message.edit_text(f"Unexpected error: {exp}")
    finally:
        if 'video_file' in locals() and os.path.exists(video_file):
            os.remove(video_file)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))