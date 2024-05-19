import datetime

import disnake
from disnake.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='мьют', description='Выдаёт мьют участнику сервера')
    @commands.has_permissions(moderate_members=True)
    async def mute(self, interaction, user: disnake.User, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        cool_time = disnake.utils.format_dt(time, style='R')
        bot_reason = f'Модератор: {interaction.author.name}. Причина: {reason}'

        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/mute"',
            description=f'Участник <@{user.id}> был замьючен.\nПо причине: ****{reason}****\nМодератор: <@{interaction.author.id}>\nРазмьют: ****{cool_time}****.',
            color=disnake.Color.yellow()
        )

        embed_user = disnake.Embed(
            title=f'Вы были замьючены на сервере {interaction.guild.name}',
            description=f'По причине: ****{reason}****\nМодератор: <@{interaction.author.id}>\nРазмьют: ****{cool_time}****.',
            color=disnake.Color.yellow()
        )

        await interaction.response.send_message(embed=embed_notf)
        await user.send(embed=embed_user)
        await interaction.guild.timeout(user, until=time, reason=bot_reason)

    @commands.slash_command(name='размьют', description='Размьючивает участника сервера')
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, interaction, user: disnake.User):
        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/unmute"',
            description=f'Участник <@{user.id}> был разамьючен\nМодератор: <@{interaction.author.id}>.',
            color=disnake.Color.green()
        )

        embed_user = disnake.Embed(
            title=f'Вы были разамьючены на сервере {interaction.guild.name}',
            description=f'Модератор: <@{interaction.author.id}>.',
            color=disnake.Color.green()
        )

        await interaction.guild.timeout(user, until=None, reason=None)
        await interaction.response.send_message(embed=embed_notf)
        await user.send(embed=embed_user)


def setup(bot):
    bot.add_cog(Mute(bot))
