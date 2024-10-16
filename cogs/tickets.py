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
        elif self.arg == '3ddesigner':
            title = 'Набор на должность 3Д художника'
        else:
            title = 'ВОЗНИКЛА ОШИБКА, СООБЩИТЕ ОБ ЭТОМ СОЗДАТЕЛЮ И ПЕРЕСОЗДАЙТЕ ФОРМУ'
        super().__init__(title=title, components=components, custom_id='ticketsModal')

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name = interaction.text_values["name"]
        age = interaction.text_values["age"]
        biography = interaction.text_values["biography"]
        wish = interaction.text_values["wish"]

        channel = interaction.guild.get_channel(1243095428593881149)  # Канал, в который будут отправляться заявки

        embed_notf = disnake.Embed(
            title='Заявка была успешно отправленна!',
            description='Чуть позже с вами свяжется модератор для дальнейшего обсуждения действий.',
            color=disnake.Color.green()
        )
        embed_notf.set_thumbnail(url=interaction.author.display_avatar.url)

        embed_post = disnake.Embed(
            title=f'Заявка на должность: {self.arg}',
            description=f'Форма была заполнена участником сервера: <@{interaction.author.id}>\n'
                        f'# Форма:'
                        f'\n\nИмя: \n****{name}****\n'
                        f'\nВозраст: \n****{age}****\n'
                        f'\nО себе: \n****{biography}****\n'
                        f'\nПочему хочет в комманду: \n****{wish}****\n'
        )

        await interaction.response.send_message(embed=embed_notf, ephemeral=True)
        await channel.send(embed=embed_post)


class TicketsSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Кодер', value='coder', description='Создаёт игровые механики и программирует оружие'),
            disnake.SelectOption(label='3Д дизайнер', value='3ddesigner', description='Создаёт или находит модели оружия, персонажей и тд.'),
            disnake.SelectOption(label='Создатель карт', value='mapmaker', description='Создаёт или изменяет Gmod карты'),
            disnake.SelectOption(label='Нарративный дизайнер', value='narrativedesigner', description='Пишет сюжет, диалоги и продумывает игровые механики')
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

    @commands.slash_command(name='тикеты-лс-принят')
    @commands.has_permissions(administrator=True)
    async def dm_tickets_accept(
            self,
            interaction,
            user: disnake.Member = commands.Param(name='участник', description="Упомяните или введите id участника"),
            current_post: str = commands.Param(name='должность', description='Введите занимаемую пользователем должность', choices=['Нарративный дизайнер', '3Д дизайнер', 'Создатель карт', 'Кодер']),
    ):
        embed_dm = disnake.Embed(
            title='Ваша заявка была рассмотрена модераторами',
            description=f'****{user.display_name}****, вы были приняты в комманду ****{interaction.guild.name}****!\n'
                        f'Выбранная вами должность: ****{current_post}****',
            color=disnake.Color.blue()
        )
        embed_notf = disnake.Embed(
            title='Сообщение было успешно отправленно!',
            description=f'Получатель: ****{user.name}****.\n'
                        f'Выбранная должность: ****{current_post}****.',
            color=disnake.Color.blurple()
        )

        await user.send(embed=embed_dm)
        await interaction.response.send_message(embed=embed_notf, ephemeral=True)

    @commands.slash_command(name='тикеты-лс-отклонено')
    @commands.has_permissions(administrator=True)
    async def dm_tickets_decline(
            self,
            interaction,
            user: disnake.Member = commands.Param(name='участник', description="Упомяните или введите id участника"),
            current_post: str = commands.Param(name='должность', description='Введите занимаемую пользователем должность', choices=['Нарративный дизайнер', '3Д художник', 'Создатель карт', 'Кодер']),
    ):
        embed_dm = disnake.Embed(
            title='Ваша заявка была рассмотрена модераторами',
            description=f'****{user.display_name}****, к сожалению вы нам не подходите!\n'
                        f'С уважением: Администрация ****{interaction.guild.name}****\n'
                        f'Выбранная вами должность: ****{current_post}****',
            color=disnake.Color.red()
        )
        embed_notf = disnake.Embed(
            title='Сообщение было успешно отправленно!',
            description=f'Получатель: ****{user.name}****.\n'
                        f'Отклонённая выбранная должность: ****{current_post}****.',
            color=disnake.Color.blurple()
        )

        await user.send(embed=embed_dm)
        await interaction.response.send_message(embed=embed_notf, ephemeral=True)

    @commands.slash_command(name='тикеты-лс-изган')
    @commands.has_permissions(administrator=True)
    async def dm_tickets_kick(
            self,
            interaction,
            user: disnake.Member = commands.Param(name='участник', description="Упомяните или введите id участника"),
            current_post: str = commands.Param(name='должность',
                                               description='Введите должность с которой был изгнан пользователь',
                                               choices=['Нарративный дизайнер', '3Д художник', 'Создатель карт', 'Кодер']),
    ):
        embed_dm = disnake.Embed(
            title=f'Вы были изгнаны из команды ****{interaction.guild.name}****',
            description=f'****{user.display_name}****, вы были изгнаны из комманды ****{interaction.guild.name}****!\n'
                        f'Ваше выполние работы не сходиться с нашими требованиями вследствии чего мы были вынуждены изгнать вас.\n'
                        f'Потерянная должность: ****{current_post}****\n'
                        f'У вас есть возможность вновь вернуться в нашу команду, но с определёнными условиями и через некоторое время.',
            color=disnake.Color.red()
        )
        embed_notf = disnake.Embed(
            title='Сообщение было успешно отправленно!',
            description=f'Получатель: ****{user.name}****.\n'
                        f'Изган с должности: ****{current_post}****.',
            color=disnake.Color.blurple()
        )

        await user.send(embed=embed_dm)
        await interaction.response.send_message(embed=embed_notf, ephemeral=True)

    @commands.command(name='тикеты', aliases=['ticket'])
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        view = disnake.ui.View()
        view.add_item(TicketsSelect())

        embed = disnake.Embed(
            title=f'Набор в команду ****{ctx.guild.name}****!',
            description='Доступны всего 3 вакансии:\n'
                        'Кодер, 3Д художник, Создатель карт, [Нарративный дизайнер](https://ru.wikipedia.org/wiki/Нарративный_дизайнер)',
            color=disnake.Color.lighter_grey()
        )

        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(TicketsSelect())
        self.bot.add_view(view, message_id=1296117579970121810)  # id сообщения после отправки комманды


def setup(bot):
    bot.add_cog(Tickets(bot))
