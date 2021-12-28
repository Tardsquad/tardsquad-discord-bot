import abc

from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.textcolor import TextColor


# See https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/cog.py#L48
class CogABCMeta(commands.CogMeta, abc.ABCMeta):
    pass


class TardBotCog(commands.Cog, metaclass=CogABCMeta):
    def __init__(self, bot, guild, *args, **kwargs):
        self.bot = bot
        self.guild = guild
