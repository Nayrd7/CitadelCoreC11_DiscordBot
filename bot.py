import disnake
from disnake.ext import commands

import config.config as cfg

from pathlib import Path

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='config/bot_token.env')


intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=cfg.bot_prefix, help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Bot - {bot.user.name} - is ready to work.")


path_cogs = Path("cogs")
for file in os.listdir(path_cogs):
    if file.endswith(',py'):
        bot.load_extension(f'cogs.{file[:-3]}')

BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(BOT_TOKEN)
