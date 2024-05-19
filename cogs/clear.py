import disnake
from disnake.ext import commands

import config.config as cfg


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='очистить', description='Удаляет указанное колличество сообщений с чата')
    @commands.has_permissions(administrator=True)
    async def clear(
            self,
            interaction,
            amout: int = commands.Param(name='колличество', description="Введите колличество сообщений, которые нужно удалить")
    ):
        embed = disnake.Embed(
            description='# Чат был очищен',
            colour=0x3fe24a
        )
        embed.add_field(
            name='Модератор:',
            value=f'<@{interaction.author.id}>',
            inline=False
        )
        embed.add_field(
            name='Колличество очищенных сообщений:',
            value=f'{amout}',
            inline=False
        )
        embed.set_image(f'{cfg.placeholder_hide}')

        await interaction.channel.purge(limit=amout + 1)
        await interaction.response.send_message(f'<@{interaction.author.id}>, операция была выполнена успешно',
                                                ephemeral=True)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Clear(bot))
