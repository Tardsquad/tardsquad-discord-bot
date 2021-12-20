import re

import discord
from discord.ext import commands

import tardsquad_discord_bot


class TardsquadClient(commands.Bot):
    def __init__(self, guild, *args, **kwargs):
        self.guild = guild
        super().__init__(command_prefix="!", *args, **kwargs)

    async def on_message(self, message):
        await super().on_message(message)
        await self._intercept(message)

    async def _intercept(self, message):
        if message.author.bot:
            return

        if re.search(r"\bljunghusen|höllviken\b", message.content, re.I):
            await message.channel.send(f"{message.author.mention} Are you sure it was on the right side of the Kanalen?")
