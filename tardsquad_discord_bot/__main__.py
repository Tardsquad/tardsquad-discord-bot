# Entry point when called as a module
# $ python -m taiga_stats

import os
import sys

import discord
from dotenv import load_dotenv


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    client = discord.Client()
    client.run(TOKEN)


if __name__ == "__main__":
    sys.exit(main())
