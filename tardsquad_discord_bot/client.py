import discord
from discord.ext import commands

import tardsquad_discord_bot


class TardsquadClient(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, command_prefix="!", **kwargs)
