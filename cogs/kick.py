import disnake
from disnake.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='кик')
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction, user: disnake.User, reason: str):
        bot_reason = f'Модератор: {interaction.author.name}. Причина кика: {reason}.'

        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/kick"',
            description=f'Участник <@{user.id}> был кикнут с сервера.\nПо причине: ****{reason}****\nМодератор: <@{interaction.author.id}>.',
            color=disnake.Color.red()
        )

        embed_user = disnake.Embed(
            title='Уведомление о кике',
            description=f'Вы были кикнуты с сервера ****{interaction.guild.name}****\nПо причине: ****{reason}****\nМодератор: <@{interaction.author.id}>.',
            color=disnake.Color.red()
        )

        await interaction.response.send_message(embed=embed_notf)
        await user.send(embed=embed_user)
        await interaction.guild.kick(user=user, reason=bot_reason)


def setup(bot):
    bot.add_cog(Kick(bot))
