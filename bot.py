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
    print(f"Bot - {bot.user.name}#{bot.user.discriminator} - is ready to work.")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(cfg.member_join))

    embed = disnake.Embed(
        title='На сервере замечен новый участник!',
        description=f"<@{member.id}>, добро пожаловать на сервер!",
        colour=disnake.Color.green()
    )

    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(cfg.member_leave))

    embed = disnake.Embed(
        title='На сервере замечена пропажа!',
        description=f"<@{member.id}> покинул сервер!",
        colour=disnake.Color.red()
    )

    await channel.send(embed=embed)


@bot.event
async def on_member_update(before, after):
    if before.premium_since is None and after.premium_since is not None:
        channel = bot.get_channel(int(cfg.member_boost))
        embed = disnake.Embed(
            title='Сервер был запущен',
            description=f'{after.name}, большое спасибо друг!',
            colour=disnake.Color.purple()
        )

        await channel.send(embed=embed)


path_cogs = Path("cogs")
for file in os.listdir(path_cogs):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(BOT_TOKEN)
