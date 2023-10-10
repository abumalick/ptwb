# Python Telegram Webapp boilerplate

## Summary

This repository contains a boilerplate for a Telegram bot that can be deployed to Heroku.

It uses the following technologies:

- [telegram-web-app.js](https://core.telegram.org/bots/webapps#initializing-mini-apps) Telegram Webapp JS library
- [python-telegram-bot](https://python-telegram-bot.org/): A python wrapper for the Telegram Bot API
- [FastAPI](https://fastapi.tiangolo.com/): A web framework for building APIs (It serves the html, css and js files needed for the webapp)
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/): A modern and designer-friendly templating language for Python.

## Project Files

- `.env`: The file that contains the environment variables (you need to create it by copying .env.example)
- `main.py`: The main file that starts the FastAPI server and initializes the bot.
- `templates/index.html`: The Jinja2 templates file that contains the webapp
- `static`: The folder that contains the static files (css, js, images, etc.)
- `requirements.txt`: The file that contains the python dependencies.

## Getting started

### Obtain a bot token

To obtain a token you need to contact [@BotFather](https://t.me/botfather) on telegram, issue the `/newbot` command and follow the steps until you're given a new token. You can find a step-by-step guide [here](https://core.telegram.org/bots/features#creating-a-new-bot).

After obtaining the bot token, copy `.env.example` to `.env` and paste the token after `BOT_TOKEN=`.

It should look like:

```
BOT_TOKEN=4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc
```

### Getting started locally

You need to have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed. It is recommended to create a virtual environment for the project.

```bash
python -m venv .venv

# you need to activate the virtual environment on every new terminal using the following command:
source .venv/bin/activate
```

#### Install dependencies

```bash
python -m pip install -r requirements.txt
```

#### Start the app

```bash
python -m pip install -r requirements.txt
```

You should be able to access the webapp at http://127.0.0.1:5000

#### Serve the web app on the global web from local environment

To serve your web app on the web from local environment, you need to make your local environment available on the web. One of the simplest solutions is to use [serveo.net](https://serveo.net/).

To use it run the following command (the first part is the subdomain you should change it to something unique to your app)

```bash
ssh -R ptw-boilerplate:80:127.0.0.1:5000 serveo.net
```

After launching the command, two links should show in the console for you to sign up using google or github. Sign in, kill the terminal process with `CTRL+C`, launch again the same command and you should be able to access your webapp at `https://ptw-boilerplate.serveo.net`.

#### Create the webapp with BotFather on telegram

After this, contact [@BotFather](https://t.me/botfather) and create a webapp by issuing the command: `/newapp` and follow the steps. You will need to provide an image whose dimensions `640x360` and the webapp url that will be `https://ptw-boilerplate.serveo.net` during development.

#### Access the web app from telegram

After creating the webapp, you should be able to access it from telegram by clicking the `Open` button in the bot.

You can find a sample bot at t.me/a_catalog_bot
