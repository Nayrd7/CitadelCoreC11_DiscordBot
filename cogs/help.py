import disnake
from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help')
    async def help(self, interaction):
        embed = disnake.Embed(
            color=0xffffff
        )
        embed.add_field(name='Доступные комманды:', value='', inline=True)

        await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Help(bot))
