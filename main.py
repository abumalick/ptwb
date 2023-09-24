import asyncio
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
PORT = os.environ.get("PORT", 5000)

tg_app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


start_handler = CommandHandler("start", start)
tg_app.add_handler(start_handler)


web_app = FastAPI()
web_app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@web_app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


web_server = uvicorn.Server(
    config=uvicorn.Config(
        app="main:web_app",
        port=PORT,
        log_level="info",
        # use_colors=False,
        host="127.0.0.1",
    )
)


async def main():
    async with tg_app:
        await tg_app.start()
        await tg_app.updater.start_polling()
        # Start other asyncio frameworks here
        await web_server.serve()
        # Stop the other asyncio frameworks here
        await tg_app.updater.stop()
        await tg_app.stop()


if __name__ == "__main__":
    asyncio.run(main())
