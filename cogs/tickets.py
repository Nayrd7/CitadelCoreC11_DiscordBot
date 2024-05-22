import disnake
from disnake.ext import commands


class TicketsModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg  # arg получается из TicketsSelect

        components = [
            disnake.ui.TextInput(label="Имя", placeholder="Введите ваше имя", custom_id='name'),
            disnake.ui.TextInput(label="Возраст", placeholder="Введите ваш возраст", custom_id='age'),
            disnake.ui.TextInput(label="Расскажите о себе", placeholder="Ваша биография", custom_id='biography'),
            disnake.ui.TextInput(label="Расскажите почему вы хотите в комманду", placeholder="Ваш текст", custom_id='wish'),
        ]
        if self.arg == 'narrativedesigner':
            title = 'Набор на должность нарративного дизайнера'
        elif self.arg == 'coder':
            title = 'Набор на должность кодера'
        elif self.arg == 'mapmaker':
            title = 'Набор на должность создателя карт'
        else:
            title = 'ВОЗНИКЛА ОШИБКА, СООБЩИТЕ ОБ ЭТОМ СОЗДАТЕЛЮ И ПЕРЕСОЗДАЙТЕ ФОРМУ'
        super().__init__(title=title, components=components, custom_id='ticketsModal')

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name = interaction.text_values["name"]
        age = interaction.text_values["age"]
        biography = interaction.text_values["biography"]
        wish = interaction.text_values["wish"]

        channel = interaction.guild.get_channel(1242911735766319115)  # Канал, в который будут отправляться заявки

        embed_notf = disnake.Embed(
            title='Заявка была успешно отправленна!',
            description='Чуть позже с вами свяжется модератор для дальнейшего обсуждения действий.',
            color=disnake.Color.green()
        )
        embed_notf.set_thumbnail(url=interaction.author.display_avatar.url)

        embed_post = disnake.Embed(
            title=f'Заявка на должность: {self.arg}',
            description='Форму была заполнена участником сервера: <@{interaction.author.id}>\n'
                        f'Форма:'
                        f'Имя: {name}'
                        f'Возраст: {age}'
                        f'О себе: {biography}'
                        f'Почему хочет в комманду: {wish}'
        )

        await interaction.response.send_message(embed=embed_notf, ephemeral=True)
        await channel.send(embed=embed_post)


class TicketsSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Кодер', value='coder', description='Создаёт игровые механики и программирует оружие'),
            disnake.SelectOption(label='Создатель карт', value='mapmaker', description='Создаёт карты для сервера'),
            disnake.SelectOption(label='Нарративный дизайнер', value='narrativedesigner', description='Пишет сюжет и диалоги и продумывает механики')
        ]
        super().__init__(
            placeholder='Выбери желаемую вакансию', options=options, min_values=0, max_values=1, custom_id='ticket'
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(TicketsModal(interaction.values[0]))


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command(name='тикеты', aliases=['ticket'])
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        view = disnake.ui.View()
        view.add_item(TicketsSelect())

        embed = disnake.Embed(
            title=f'Набор в команду ****{ctx.guild.name}****!',
            description='Доступны всего 3 вакансии:\n'
                        'Кодер, Создатель карт, [Нарративный дизайнер](https://ru.wikipedia.org/wiki/Нарративный_дизайнер)',
            color=disnake.Color.lighter_grey()
        )

        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(TicketsSelect())
        self.bot.add_view(view, message_id=...)  # id сообщения после отправки комманды


def setup(bot):
    bot.add_cog(Tickets(bot))
