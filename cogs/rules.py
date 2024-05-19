import disnake
from disnake.ext import commands

import datetime
import config.config as cfg


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rules', aliases=['правила'])
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):
        time = datetime.datetime.now()
        cool_time = disnake.utils.format_dt(time, style="R")

        category1 = disnake.Embed(color=0xff0000, description='# Конфликты:')
        category1.set_image(f'{cfg.placeholder}')

        rule1 = disnake.Embed(color=0xff0000)
        rule1.add_field(name='', value='> ****1.1 • Оскорбления / унижение / угрозы в адрес участников****', inline=False)
        rule1.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule1.add_field(name='Срок:', value='```1 → 4 часа```', inline=True)
        rule1.set_image(f'{cfg.placeholder}')

        rule2 = disnake.Embed(color=0xff0000)
        rule2.add_field(name='', value='> ****1.2 • Неадекватное / токсичное поведение****', inline=False)
        rule2.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule2.add_field(name='Срок:', value='```4 → 8 → 12 часов```', inline=True)
        rule2.set_image(f'{cfg.placeholder}')

        rule3 = disnake.Embed(color=0xff0000)
        rule3.add_field(name='', value='> ****1.3 • Разведение / поддержка конфликтных ситуаций****', inline=False)
        rule3.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule3.add_field(name='Срок:', value='```3 → 7 дней```', inline=True)
        rule3.set_image(f'{cfg.placeholder}')

        rule4 = disnake.Embed(color=0xff0000)
        rule4.add_field(name='', value='> ****1.4 • Провокация участников на совершение нарушений****', inline=False)
        rule4.add_field(name='Наказание:', value='```Мьют / Бан```', inline=True)
        rule4.add_field(name='Срок:', value='```7 дней / Перманентно```', inline=True)
        rule4.set_image(f'{cfg.placeholder}')

        rule5 = disnake.Embed(color=0xff0000)
        rule5.add_field(name='', value='> ****1.5 • Слив личных данных участников****', inline=False)
        rule5.add_field(name='Наказание:', value='```Бан```', inline=True)
        rule5.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule5.set_image(f'{cfg.placeholder}')

        rule6 = disnake.Embed(color=0xff0000)
        rule6.add_field(name='', value='> ****1.6 • Обсуждение и публикация политических и военных тем, а также провокационные высказывания своих взглядов на эти темы и т.д.****', inline=False)
        rule6.add_field(name='Наказание:', value='```Мьют / Бан```', inline=True)
        rule6.add_field(name='Срок:', value='```3 → 7 дней / Перманентно```', inline=True)
        rule6.set_image(f'{cfg.placeholder}')

        rule7 = disnake.Embed(color=0xff0000)
        rule7.add_field(name='', value='> ****1.7 • Откровенная травля, клевета, распускание ложных слухов об участниках сервера****', inline=False)
        rule7.add_field(name='Наказание:', value='```Бан```', inline=True)
        rule7.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule7.set_image(f'{cfg.placeholder}')

        rule8 = disnake.Embed(color=0xff0000)
        rule8.add_field(name='', value='> ****1.8 • Разногласия на тему расы, национальности и т.д.****', inline=False)
        rule8.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule8.add_field(name='Срок:', value='```1 → 3 → 7 дней```', inline=True)
        rule8.set_image(f'{cfg.placeholder}')

        rule9 = disnake.Embed(color=0xff0000)
        rule9.add_field(name='', value='> ****1.9 • Злоупотребление правами особых ролей****', inline=False)
        rule9.add_field(name='Наказание:', value='```Лишение роли```', inline=True)
        rule9.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule9.set_image(f'{cfg.placeholder}')

        rule10 = disnake.Embed(color=0xff0000)
        rule10.add_field(name='', value='> ****1.10 • Шумы / посторонние звуки, мешающие участникам голосового чата****', inline=False)
        rule10.add_field(name='Наказание:', value='```Мьют микрофона```', inline=True)
        rule10.add_field(name='Срок:', value='```До исправления```', inline=True)
        rule10.set_image(f'{cfg.placeholder}')

        rule11 = disnake.Embed(color=0xff0000)
        rule11.add_field(name='', value='> ****1.11 • Использование звуковых устройства без разрешения участников голосового канала(Soundpad и тд.)****', inline=False)
        rule11.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule11.add_field(name='Срок:', value='```4 → 24 часа```', inline=True)
        rule11.set_image(f'{cfg.placeholder}')

        category2 = disnake.Embed(color=0xff0000, description='# Чат и общение:')
        category2.set_image(f'{cfg.placeholder}')

        rule12 = disnake.Embed(color=0xff0000)
        rule12.add_field(name='', value='> ****2.1 • Использование каналов не по назначению****', inline=False)
        rule12.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule12.add_field(name='Срок:', value='```1 → 4 → 12 часов```', inline=True)
        rule12.set_image(f'{cfg.placeholder}')

        rule13 = disnake.Embed(color=0xff0000)
        rule13.add_field(name='', value='> ****2.2 • Спам, флуд, капс****', inline=False)
        rule13.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule13.add_field(name='Срок:', value='```2 → 6 → 24 часов```', inline=True)
        rule13.set_image(f'{cfg.placeholder}')

        rule14 = disnake.Embed(color=0xff0000)
        rule14.add_field(name='', value='> ****2.3 • Публикация и демонстрация любого вида контента NSFW в не предназначенных для этого каналах****', inline=False)
        rule14.add_field(name='Наказание:', value='```Мьют / Бан```', inline=True)
        rule14.add_field(name='Срок:', value='```1 → 4 → 7 дней / Перманентно```', inline=True)
        rule14.set_image(f'{cfg.placeholder}')

        rule15 = disnake.Embed(color=0xff0000)
        rule15.add_field(name='', value='> ****2.4 • Публикация и демонстрация любого вида контента NSFL****', inline=False)
        rule15.add_field(name='Наказание:', value='```Бан```', inline=True)
        rule15.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule15.set_image(f'{cfg.placeholder}')

        rule16 = disnake.Embed(color=0xff0000)
        rule16.add_field(name='', value='> ****2.5 • Нацизм, фашизм и т.д.****', inline=False)
        rule16.add_field(name='Наказание:', value='```Бан```', inline=True)
        rule16.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule16.set_image(f'{cfg.placeholder}')

        rule17 = disnake.Embed(color=0xff0000)
        rule17.add_field(name='', value='> ****2.6 • Реклама в любом виде****', inline=False)
        rule17.add_field(name='Наказание:', value='```Мьют / Бан```', inline=True)
        rule17.add_field(name='Срок:', value='```1 → 7 дней / Перманентно```', inline=True)
        rule17.set_image(f'{cfg.placeholder}')

        rule18 = disnake.Embed(color=0xff0000)
        rule18.add_field(name='', value='> ****2.7 • Публикация вредоносных материалов****', inline=False)
        rule18.add_field(name='Наказание:', value='```Мьют / Бан```', inline=True)
        rule18.add_field(name='Срок:', value='```30 дней / Перманентно```', inline=True)
        rule18.set_image(f'{cfg.placeholder}')

        rule19 = disnake.Embed(color=0xff0000)
        rule19.add_field(name='', value='> ****2.8 • Публикация видео и ссылок, содержащих скримеры без предупреждения****', inline=False)
        rule19.add_field(name='Наказание:', value='```Мьют```', inline=True)
        rule19.add_field(name='Срок:', value='```1 → 4 → 24 часа```', inline=True)
        rule19.set_image(f'{cfg.placeholder}')

        rule20 = disnake.Embed(color=0xff0000)
        rule20.add_field(name='', value='> ****2.9 • Публикация/демонстрация экстремистского контента на сервере****', inline=False)
        rule20.add_field(name='Наказание:', value='```Бан```', inline=True)
        rule20.add_field(name='Срок:', value='```Перманентно```', inline=True)
        rule20.set_image(f'{cfg.placeholder}')

        embed_update_time = disnake.Embed(color=0xff0000, title=f'Последнее обновление правил было: {cool_time}')
        embed_update_time.set_image(f'{cfg.placeholder}')

        await ctx.purge
        await ctx.send(embeds=[category1, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
        await ctx.send(embeds=[rule10, rule11, category2, rule12, rule13, rule14, rule15, rule16, rule17, rule18])
        await ctx.send(embeds=[rule19, rule20, embed_update_time])

# await ctx.send(embeds=[category1, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, category2, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, embed_update_time])


def setup(bot):
    bot.add_cog(Rules(bot))
