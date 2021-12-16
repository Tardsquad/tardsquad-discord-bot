# Entry point when called as a module
# $ python -m taiga_stats

import os
import sys

from discord import Client, Embed, Intents
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv


@slash.slash(name="test")
async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = Client(intents=Intents.default())
    slash = SlashCommand(bot)
    bot.run(TOKEN)


if __name__ == "__main__":
    sys.exit(main())
