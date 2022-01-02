import functools
import logging
import re

import requests
import semver
from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.cog import TardBotCog


class TardBotMetaCommands(TardBotCog, name="BotMeta"):
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Logged on as {self.bot.user} at server {self.guild}.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        logging.info(f"Disconnecting from server {self.guild}.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            reply = f"{ctx.message.author.mention} Required parameters for the command are missing. Please check `!help {ctx.command}`"
            await ctx.send(reply)

    @commands.command(help="Print my bot version.")
    async def version(self, ctx):
        url = "https://api.github.com/repos/Tardsquad/tardsquad-discord-bot/tags"
        resp = requests.get(url=url)
        latest_ver = None
        if resp.status_code == 200:
            versions = []
            for tag in resp.json():
                if re.match(r"^v\d+\.", tag["name"]):
                    versions.append(tag["name"][1:])
            if versions:
                latest_ver = max(versions, key=functools.cmp_to_key(semver.compare))

        reply = f"I'm at `v{tardsquad_discord_bot.__version__}`."
        if latest_ver and latest_ver != semver.VersionInfo.parse(tardsquad_discord_bot.__version__):
            reply += "\nHowever the latest version pushed to GitHub is `v{:s}`".format(str(latest_ver))
        await ctx.send(reply)

    @commands.command(help="Get the link to my source code.")
    async def source(self, ctx):
        repo_url = "https://github.com/Tardsquad/tardsquad-discord-bot"
        reply = "**Please extend me** with more commands by contributing to:\n<{:s}>".format(repo_url)
        await ctx.send(reply)

    @commands.command(help="Get the link to my application deployment status.")
    async def deployment(self, ctx):
        revision_url = "https://console.cloud.google.com/run/detail/us-central1/tardsquad-discord-bot/revisions?project=tardsquad-discord-bot"
        reply = "The latest & ongoing deployments can be found at:\n<{:s}>".format(revision_url)
        await ctx.send(reply)
