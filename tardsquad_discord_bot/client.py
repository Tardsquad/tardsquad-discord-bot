import logging

import discord


class TardsquadClient(discord.Client):
    def __init__(self, guild, *args, **kwargs):
        self.guild = guild
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        logging.info(f"Logged on as {self.user} at {self.guild}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!rot13"):
            text = message.content[len("!rot13") :]
            textrot = codecs.encode(text, "rot_13")
            reply = "*rot13 of that is:*\n{:s}".format(textrot)
            await message.channel.send(reply)
