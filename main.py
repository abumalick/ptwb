import asyncio
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
    MenuButtonWebApp,
    WebAppInfo,
)
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 5000))
WEB_APP_URL = os.environ["WEB_APP_URL"]

tg_app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
tg_web_app = WebAppInfo(WEB_APP_URL)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.effective_chat:
        # Inline button
        keyboard = [[InlineKeyboardButton("Start App", web_app=tg_web_app)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Welcome to the catalog, to see our products click one of the buttons.",
            reply_markup=reply_markup,
        )

        # menu button
        menu_button_web_app = MenuButtonWebApp("Start App", tg_web_app)
        await context.bot.set_chat_menu_button(
            chat_id=update.effective_chat.id, menu_button=menu_button_web_app
        )


start_handler = CommandHandler("start", start)
tg_app.add_handler(start_handler)
# add MenuButtonWebApp

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
        if tg_app.updater:
            await tg_app.updater.start_polling()
        # Start other asyncio frameworks here
        await web_server.serve()
        # Stop the other asyncio frameworks here
        if tg_app.updater:
            await tg_app.updater.stop()
        await tg_app.stop()


if __name__ == "__main__":
    asyncio.run(main())
