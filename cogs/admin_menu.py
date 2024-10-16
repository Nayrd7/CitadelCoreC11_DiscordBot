import disnake
from disnake.ext import commands


class AdmmenuModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label='Введите ID канала',
                placeholder='ID канала',
                custom_id='id_channel',
            ),
            disnake.ui.TextInput(
                label='Введите название поста',
                placeholder='Название поста',
                custom_id='title',
            ),
            disnake.ui.TextInput(
                label='Введите содержимое поста',
                placeholder='Содержимое поста',
                custom_id='content',
            ),
            disnake.ui.TextInput(
                label='Введите цвет поста',
                placeholder='HEX формат цвета(без знака #):',
                custom_id='hex_color',
            ),
            disnake.ui.TextInput(
                label='Вставьте ссылку на картинку',
                placeholder='Ссылка должна выглядеть примерно так: https://example.com/fmkgmdk',
                custom_id='image',
            )
        ]

        super().__init__(title='Отправка поста в канал', components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        id_channel = interaction.text_values["id_channel"]
        title = interaction.text_values["title"]
        content = interaction.text_values["content"]
        hex_color = interaction.text_values["hex_color"]
        image = interaction.text_values["image"]

        embed_post = disnake.Embed(
            title=title,
            description=content,
            colour=int(hex_color, 16)
        )

        if image == '0':
            pass
        else:
            embed_post.set_image(url=image)

        embed_notification = disnake.Embed(
            description='Пост был опубликован!',
            colour=0x00ff00
        )

        channel = interaction.guild.get_channel(int(id_channel))

        await channel.send('> @everyone', embed=embed_post)
        await interaction.response.send_message(embed=embed_notification, ephemeral=True)


class AdmmenuButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="📢 Опубликовать пост", style=disnake.ButtonStyle.green, custom_id="admmenubutton1")
    async def admmenubutton1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        modal = AdmmenuModal()
        await interaction.response.send_modal(modal)

    # @disnake.ui.button(label="📟 Написать участнику в лс", style=disnake.ButtonStyle.green, custom_id="admmenubutton2")
    # async def admmenubutton1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # modal = AdmmenuModal()
        # await interaction.response.send_modal(modal)


class AdmmenuModalSend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.command(name='админменю', aliases=['admmenu'], description='Устанавливает панель администратора')
    @commands.has_permissions(administrator=True)
    async def admmenu(self, interaction: disnake.AppCmdInter):
        view = AdmmenuButton()

        embed = disnake.Embed(colour=0xff0000)
        embed.title = 'Панель администрации.'
        embed.description = f'Панель администрации упростит вам жизнь!\n' \
                            'Зачем это нужно? - она создана для того, чтобы не перебирать сотни комманд для отправки одного поста, ' \
                            'а по нажатию одной кнопки выполнить нужное вам действие, пользуйтесь!\n' \
                            'Как её использовать? - всё очень просто! Нажимаете кнопку, вводите нужные данные и воуля!'

        await interaction.channel.purge(limit=1)
        await interaction.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        # Message ID сообщения, где будет кнопка, добавляется после отправки команды.
        self.bot.add_view(AdmmenuButton(), message_id=1241755472642441392)


def setup(bot):
    bot.add_cog(AdmmenuModalSend(bot))
