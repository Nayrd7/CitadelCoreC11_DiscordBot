import disnake
from disnake.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='кик', description='Выгоняет участника с сервера, с возможностью возврата')
    @commands.has_permissions(kick_members=True)
    async def kick(
            self,
            interaction,
            user: disnake.User = commands.Param(name='участник', description="Упомяните или введите id участника"),
            reason: str = commands.Param(name='причина', description='Введите причину кика')
    ):
        bot_reason = f'Модератор: {interaction.author.name}. Причина кика: {reason}.'

        if interaction.guild.get_member(user.id) is None:
            embed_notf = disnake.Embed(
                title='',
                description=f'Участник не был найден на сервере.',
                color=disnake.Color.green()
            )
            await interaction.response.send_message(embed=embed_notf, ephemeral=T1rue)
            return

        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/kick"',
            description=f'Участник <@{user.id}> был кикнут с сервера.\nПо причине: ****{reason}****\nМодератор: <@{interaction.author.id}>.',
            color=disnake.Color.red()
        )

        embed_user = disnake.Embed(
            title=f'Вы были кикнуты с сервера ****{interaction.guild.name}****',
            description=f'По причине: ****{reason}****\nМодератор: <@{interaction.author.id}>.',
            color=disnake.Color.red()
        )

        await interaction.response.send_message(embed=embed_notf)
        await user.send(embed=embed_user)
        await interaction.guild.kick(user=user, reason=bot_reason)


def setup(bot):
    bot.add_cog(Kick(bot))
