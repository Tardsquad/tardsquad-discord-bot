import codecs
import logging
from operator import itemgetter

import discord


class TardsquadClient(discord.Client):
    def __init__(self, guild, *args, **kwargs):
        self.guild = guild
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        logging.info(f"Logged on as {self.user} at {self.guild}")

    async def on_message(self, message):
        if message.author == self.user or message.content[0] != "!":
            return

        if message.content.startswith("!help"):
            commands = [
                ("rot13", "Encode the string after the command with the rot-13 scheme."),
                ("help", "Show this help message."),
            ]
            commandstr = "\n".join(f"**!{cmd}** - {desc}" for cmd, desc in sorted(commands, key=itemgetter(0)))
            reply = "The commands that I support are:\n{:s}".format(commandstr)
            await message.channel.send(reply)

        if message.content.startswith("!rot13 "):
            text = message.content[len("!rot13 ") :]
            textrot = codecs.encode(text, "rot_13")
            reply = "*rot13 of that is:*\n{:s}".format(textrot)
            await message.channel.send(reply)
