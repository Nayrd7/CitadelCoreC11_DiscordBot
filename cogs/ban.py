import disnake
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='бан')
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter, user: disnake.User, reason: str):
        bot_reason = f'Модератор: {inter.author.name}. Причина бана: {reason}.'

        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/ban"',
            description=f'Участник <@{user.id}> Был забанен на сервере.\nПо причине: ****{reason}****.\nМодератор: <@{inter.author.id}>.',
            color=disnake.Color.red()
        )

        embed_user = disnake.Embed(
            title='Уведомление о бане',
            description=f'Вы были забанены на сервере ****{inter.guild.name}****.\nПо причине: ****{reason}****\nМодератор: ****<@{inter.author.id}>****.',
            color=disnake.Color.red()
        )

        await inter.response.send_message(embed=embed_notf)
        await user.send(embed=embed_user)
        await inter.guild.ban(user, reason=bot_reason)

    @commands.slash_command(name='разбан')
    @commands.has_permissions(ban_members=True)
    async def unban(self, inter, user: disnake.User):
        embed_notf = disnake.Embed(
            title='Модератор использовал комманду "/unban"',
            description=f'Участник <@{user.id}> Был разбанен на сервере.\nМодератор: <@{inter.author.id}>.',
            color=disnake.Color.red()
        )

        await inter.response.send_message(embed=embed_notf)
        await inter.guild.unban(user)


def setup(bot):
    bot.add_cog(Ban(bot))
