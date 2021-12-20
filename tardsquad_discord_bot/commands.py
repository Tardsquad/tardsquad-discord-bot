import codecs
import logging

from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.textcolor import TextColor

REPO_URL = "https://github.com/Tardsquad/tardsquad-discord-bot"


class TardBotCommands(commands.Cog):
    def __init__(self, bot, guild, *args, **kwargs):
        self.bot = bot
        self.guild = guild

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Logged on as {self.bot.user} at server {self.guild}.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        logging.info("Disconnecting from server {self.guild}.")

    @commands.command(help="Print my bot version.")
    async def version(self, ctx):
        reply = f"I'm at `v{tardsquad_discord_bot.__version__}`."
        # TODO maybe check if this is the latest available version and warn if we're no on that?
        # https://github.com/Tardsquad/tardsquad-discord-bot/tags
        await ctx.send(reply)

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

    @commands.command(help="Get the link to my source code.")
    async def source(self, ctx):
        reply = "**Please extend me** with more commands by contributing to\n<{:s}>".format(REPO_URL)
        await ctx.send(reply)
