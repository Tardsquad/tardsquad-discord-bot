import re

from discord.ext import commands

from tardsquad_discord_bot.interceptor_helpers import InterceptorMetaclass, message_interceptor


class TardBotInterceptors(commands.Cog, metaclass=InterceptorMetaclass):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        for interceptor in self.interceptor_methods:
            await interceptor(self, message)

    @message_interceptor()
    async def intercept_ljunghusen(self, message):
        if re.search(r"\bljunghusen|höllviken\b", message.content, re.I):
            reply = f"{message.author.mention} Are you sure it was on the right side of the Kanalen?"
            await message.channel.send(reply)

    @message_interceptor()
    async def intercept_nummer(self, message):
        if re.search(r"(?<!person)nummer\b", message.content, re.I):
            reply = f"{message.author.mention} med nummer menar du personnummer?"
            await message.channel.send(reply)

    @message_interceptor()
    async def intercept_system(self, message):
        if re.search(r"(?<!eko)system\b", message.content, re.I):
            reply = f"{message.author.mention} typ som ett ekosystem?"
            await message.channel.send(reply)

    @message_interceptor()
    async def intercept_alles_gut(self, message):
        if re.search(r"\balles\s+gut\b", message.content, re.I):
            reply = f"{message.author.mention} gut alles!"
            await message.channel.send(reply)

    @message_interceptor()
    async def intercept_gut_alles(self, message):
        if re.search(r"\bgut\s+alles\b", message.content, re.I):
            reply = f"{message.author.mention} alles gut!"
            await message.channel.send(reply)
