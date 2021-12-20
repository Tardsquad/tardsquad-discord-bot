import re

import discord
from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.message_interceptor import InterceptorMetaclass, message_interceptor


class TardsquadClient(commands.Bot, metaclass=InterceptorMetaclass):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix="!", *args, **kwargs)

    async def on_message(self, message):
        await super().on_message(message)
        await self._intercept_message(message)

    async def _intercept_message(self, message):
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
