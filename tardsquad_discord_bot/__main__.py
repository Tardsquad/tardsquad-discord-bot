# Entry point when called as a module
# $ python -m tardsquad_discord_bot

import logging
import os
import sys

import discord
from dotenv import load_dotenv

from tardsquad_discord_bot.client import TardsquadClient


def setup_logging():
    # Our log level (root).
    logging.basicConfig(level=logging.INFO)

    # Log level for discord.py package.
    disc_logger = logging.getLogger("discord")
    disc_logger.setLevel(logging.WARNING)


def read_conf():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild = os.getenv("GUILD")
    return token, guild


def main():
    setup_logging()
    token, guild = read_conf()

    client = TardsquadClient(guild)
    client.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
