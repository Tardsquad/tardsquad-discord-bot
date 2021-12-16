# Entry point when called as a module
# $ python -m taiga_stats

import codecs
import logging
import os
import sys

import discord
from dotenv import load_dotenv


class MyClient(discord.Client):
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


def setup_logging():
    # Our log level (root).
    logging.basicConfig(level=logging.INFO)

    # Log level for discord.py package.
    logger = logging.getLogger("discord")
    logger.setLevel(logging.WARNING)


def read_conf():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild = os.getenv("GUILD")
    return token, guild


def main():
    setup_logging()
    token, guild = read_conf()

    client = MyClient(guild)
    client.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
