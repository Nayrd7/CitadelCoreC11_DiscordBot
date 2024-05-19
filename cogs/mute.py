import disnake
from disnake.ext import commands

import datetime


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='мьют', description='Выдаёт мьют участнику сервера')
    @commands.has_permissions(moderate_members=True)
    async def mute(
            self,
            interaction,
            user: disnake.Member = commands.Param(name='участник', description="Упомяните или введите id участника"),
            term: str = commands.Param(name='срок', description="Введите время мьюта"),
            time: str = commands.Param(name='время', description='Введите формат времени', choices=['Дни', 'Часы', 'Минуты', 'Секунды']),
            reason: str = commands.Param(name='причина', description="Введите причину мьюта")
    ):
        if time.lower() == 'дни':
            term = datetime.datetime.now() + datetime.timedelta(days=int(term))
        elif time.lower() == 'часы':
            term = datetime.datetime.now() + datetime.timedelta(hours=int(term))
        elif time.lower() == 'минуты':
            term = datetime.datetime.now() + datetime.timedelta(minutes=int(term))
        elif time.lower() == 'секунды':
            term = datetime.datetime.now() + datetime.timedelta(seconds=int(term))
        else:
            embed_error = disnake.Embed(
                title='',
                description=f'Неверный ввод команды: Неправильно выбрано время(Секунды, Минуты, Часы, Дни)',
                color=disnake.Color.yellow()
            )
            await interaction.response.send_message(embed=embed_error, ephemeral=True)
            return

        cool_time = disnake.utils.format_dt(term, style='R')
        bot_reason = f'Модератор: {interaction.author.name}. Причина: {reason}'

        if not user.current_timeout:
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
            await interaction.guild.timeout(user, until=term, reason=bot_reason)
        else:
            embed_notf = disnake.Embed(
                title='',
                description=f'Участник <@{user.id}> уже находиться в мьюте.',
                color=disnake.Color.yellow()
            )
            await interaction.response.send_message(embed=embed_notf, ephemeral=True)

    @commands.slash_command(name='размьют', description='Размьючивает участника сервера')
    @commands.has_permissions(moderate_members=True)
    async def unmute(
            self,
            interaction,
            user: disnake.Member = commands.Param(name='участник', description="Упомяните или введите id участника")
    ):
        if user.current_timeout:
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
        else:
            embed_notf = disnake.Embed(
                title='',
                description=f'Участник <@{user.id}> не замьючен.',
                color=disnake.Color.green()
            )
            await interaction.response.send_message(embed=embed_notf, ephemeral=True)


def setup(bot):
    bot.add_cog(Mute(bot))
