# Entry point when called as a module
# $ python -m tardsquad_discord_bot

import logging
import os
import sys

from dotenv import load_dotenv

from tardsquad_discord_bot.client import TardsquadClient
from tardsquad_discord_bot.commands_general import TardBotGeneralCommands
from tardsquad_discord_bot.commands_meta import TardBotMetaCommands
from tardsquad_discord_bot.commands_rating import TardBotRatingCommands
from tardsquad_discord_bot.commands_search import TardBotSearchCommands
from tardsquad_discord_bot.gcp_port import start_gcp_port
from tardsquad_discord_bot.interceptors import TardBotInterceptors


def setup_logging():
    # Our log level (root).
    logging.basicConfig(level=logging.INFO)

    # Log level for discord.py package.
    disco_logger = logging.getLogger("discord")
    disco_logger.setLevel(logging.WARNING)

    # Log level for dummy GCP server thread.
    gcp_logger = logging.getLogger("gcp_port")
    gcp_logger.setLevel(logging.INFO)


def read_conf():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    guild = os.getenv("GUILD", "tardsquad")
    port = int(os.getenv("PORT", "8080"))
    return token, guild, port


def main():
    setup_logging()
    token, guild, port = read_conf()
    start_gcp_port(port)

    bot = TardsquadClient()
    bot.add_cog(TardBotGeneralCommands(bot, guild))
    bot.add_cog(TardBotRatingCommands(bot, guild))
    bot.add_cog(TardBotSearchCommands(bot, guild))
    bot.add_cog(TardBotMetaCommands(bot, guild))
    bot.add_cog(TardBotInterceptors(bot, guild))
    bot.run(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
