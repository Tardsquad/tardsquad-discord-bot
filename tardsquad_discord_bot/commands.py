import codecs
import functools
import logging
import re
import urllib

import requests
import semver
from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.textcolor import TextColor

REPO_URL = "https://github.com/Tardsquad/tardsquad-discord-bot"


# TODO add a "!weather <location>" command?
class TardBotCommands(commands.Cog):
    def __init__(self, bot, guild, *args, **kwargs):
        self.bot = bot
        self.guild = guild

    @staticmethod
    def search_query(url_fmt, *args):
        query = urllib.parse.quote(" ".join(args))
        url_fmt = "<" + url_fmt + ">"
        return url_fmt.format(query)

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Logged on as {self.bot.user} at server {self.guild}.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        logging.info("Disconnecting from server {self.guild}.")

    @commands.command(help="Print my bot version.")
    async def version(self, ctx):
        url = "https://api.github.com/repos/Tardsquad/tardsquad-discord-bot/tags"
        resp = requests.get(url=url)
        latest_ver = None
        if resp.status_code == 200:
            versions = []
            for tag in resp.json():
                if re.match(r"^v\d+\.", tag["name"]):
                    try:
                        versions.append(tag["name"][1:])
                    except ValueError:
                        pass
                if versions:
                    versions.sort(key=functools.cmp_to_key(semver.compare))
                    latest_ver = versions[-1]

        reply = f"I'm at `v{tardsquad_discord_bot.__version__}`."
        if latest_ver and latest_ver != semver.VersionInfo.parse(tardsquad_discord_bot.__version__):
            reply += "\nHowever the latest version is `v{:s}`".format(str(latest_ver))
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

    @commands.command(name="google", aliases=["g", "lmgtfy"], help="Search on Google for given query string.")
    async def search_google(self, ctx, *args):
        url_fmt = "https://www.google.com/search?hl=en&q={:s}"
        await ctx.send(TardBotCommands.search_query(url_fmt, *args))

    @commands.command(name="duck", aliases=["d"], help="Search on DuckDuckGo for given query string.")
    async def search_duckduckgo(self, ctx, *args):
        url_fmt = "https://duckduckgo.com/?t=ffab&q={:s}"
        await ctx.send(TardBotCommands.search_query(url_fmt, *args))

    @commands.command(name="youtube", aliases=["y", "yt"], help="Search on YouTube for given query string.")
    async def search_youtube(self, ctx, *args):
        url_fmt = "https://www.youtube.com/results?search_query={:s}"
        await ctx.send(TardBotCommands.search_query(url_fmt, *args))

    @commands.command(name="wikipedia", aliases=["w"], help="Search on Wikipedia for given query string.")
    async def search_wikipedia(self, ctx, *args):
        url_fmt = "http://en.wikipedia.org/wiki/Special:Search?search={:s}"
        await ctx.send(TardBotCommands.search_query(url_fmt, *args))

    @commands.command(name="imdb", aliases=["i"], help="Search on IMDB for given query string.")
    async def search_imdb(self, ctx, *args):
        url_fmt = "https://www.imdb.com/find?q={:s}"
        await ctx.send(TardBotCommands.search_query(url_fmt, *args))
