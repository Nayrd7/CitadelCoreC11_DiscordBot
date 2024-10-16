import disnake
from disnake.ext import commands

import config.config as cfg


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='правила-сервер', aliases=['rules-server'])
    @commands.has_role(1242902771372654653)
    async def rules_server(self, ctx):
        embed = disnake.Embed(
            title='Информация о сервере:',
            color=disnake.Color.dark_gray()
        )
        embed.add_field(
            name='Устав Альянса:',
            value=f'{cfg.regulation_alliance}',
        )
        embed.add_field(
            name='Лор:',
            value=f'{cfg.lore}',
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
