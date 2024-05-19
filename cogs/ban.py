import disnake
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='бан')
    @commands.has_permissions(ban_members=True)
    async def ban(self, interaction, user: disnake.User, reason: str):
        bot_reason = f'Модератор: {interaction.author.name}. Причина бана: {reason}.'

        try:
            await interaction.guild.fetch_ban(user)

            embed_notf = disnake.Embed(
                title='',
                description=f'Участник <@{user.id}> уже забанен на сервере.',
                color=disnake.Color.green()
            )

            await interaction.response.send_message(embed=embed_notf, ephemeral=True)
        except disnake.NotFound:
            embed_notf = disnake.Embed(
                title='Модератор использовал комманду "/ban"',
                description=f'Участник <@{user.id}> был забанен на сервере.\nПо причине: ****{reason}****.\nМодератор: <@{interaction.author.id}>.',
                color=disnake.Color.red()
            )
            embed_user = disnake.Embed(
                title=f'Вы были забанены на сервере {interaction.guild.name}.',
                description=f'По причине: ****{reason}****\nМодератор: ****<@{interaction.author.id}>****.',
                color=disnake.Color.red()
            )

            await interaction.response.send_message(embed=embed_notf)
            await user.send(embed=embed_user)
            await interaction.guild.ban(user, reason=bot_reason)

    @commands.slash_command(name='разбан')
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction, user: disnake.User):
        try:
            await interaction.guild.fetch_ban(user)
            embed_notf = disnake.Embed(
                title='Модератор использовал комманду "/unban"',
                description=f'Участник <@{user.id}> был разбанен на сервере.\nМодератор: <@{interaction.author.id}>.',
                color=disnake.Color.green()
            )

            await interaction.response.send_message(embed=embed_notf)
            await interaction.guild.unban(user)
        except disnake.NotFound:
            embed_notf = disnake.Embed(
                title='',
                description=f'Участник <@{user.id}> не забанен на сервере.',
                color=disnake.Color.green()
            )
            await interaction.response.send_message(embed=embed_notf, ephemeral=True)


def setup(bot):
    bot.add_cog(Ban(bot))
