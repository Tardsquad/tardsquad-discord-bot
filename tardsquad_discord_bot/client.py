import codecs
import logging
import re
from operator import itemgetter

import discord

import tardsquad_discord_bot


class TardsquadClient(discord.Client):
    def __init__(self, guild, *args, **kwargs):
        self.guild = guild
        super().__init__(*args, **kwargs)

    async def _handle_commands(self, message):
        if message.content.startswith("!help"):
            commands = [
                ("rot13", "Encode the string after the command with the rot-13 scheme."),
                ("help", "Show this help message."),
                ("version", "Print version of the bot"),
            ]
            commandstr = "\n".join(f"**!{cmd}** - {desc}" for cmd, desc in sorted(commands, key=itemgetter(0)))
            reply = "The commands that I support are:\n{:s}".format(commandstr)
            await message.channel.send(reply)
        elif message.content.startswith("!rot13 "):
            text = message.content[len("!rot13 ") :]
            textrot = codecs.encode(text, "rot_13")
            reply = "*rot13 of that is:*\n{:s}".format(textrot)
            await message.channel.send(reply)
        elif message.content.startswith("!version"):
            reply = f"I'm at version `{tardsquad_discord_bot.__version__}`"
            await message.channel.send(reply)

    async def _intercept(self, message):
        if re.search(r"\bljunghusen|höllviken\b", message.content, re.I):
            await message.channel.send(f"{message.author.mention} Are you sure it was on the right side of the Kanalen?")

    async def on_ready(self):
        logging.info(f"Logged on as {self.user} at server {self.guild}.")

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content[0] == "!":
            await self._handle_commands(message)
        else:
            await self._intercept(message)
