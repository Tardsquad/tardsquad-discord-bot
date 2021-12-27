import codecs

import requests
import semver
from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.textcolor import TextColor


# TODO add a "!weather <location>" command?
class TardBotGeneralCommands(commands.Cog, name="General"):
    def __init__(self, bot, guild, *args, **kwargs):
        self.bot = bot
        self.guild = guild

    @commands.command(help="Encode the string after the command with the rot-13 scheme.")
    async def rot13(self, ctx, *args):
        reply = None
        if len(args) == 0:
            reply = TextColor.orange("Error No text to rotate given as argument to this command.")
        else:
            text = " ".join(args)
            textrot = codecs.encode(text, "rot_13")
            reply = "*rot13 of that is:*\n{:s}".format(textrot)
        await ctx.send(reply)
