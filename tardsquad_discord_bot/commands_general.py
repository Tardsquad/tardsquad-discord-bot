import codecs
from itertools import groupby
from operator import attrgetter

import requests
import semver
from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.ratingentry import RatingEntry
from tardsquad_discord_bot.textcolor import TextColor


# TODO add a "!weather <location>" command?
class TardBotGeneralCommands(commands.Cog, name="General"):
    def __init__(self, bot, guild, *args, **kwargs):
        self.bot = bot
        self.guild = guild
        self.ratings = {}

    def _rating_gc(self):
        self.ratings = {aid: rating for aid, rating in self.ratings.items() if not rating.expired()}

    def _rating_status(self):
        self._rating_gc()
        if not self.ratings:
            return "*Currently no active ratings collected*\n\nPlease share your rating with the `!rate` command."
        summary = []
        sortkeyfn = attrgetter("rating")
        for rating, entries in groupby(reversed(sorted(self.ratings.values(), key=sortkeyfn)), key=sortkeyfn):
            names = [f"{entry.user.name} (expires in {entry.expires_at()})" for entry in entries]
            summary.append(f"* {rating}: {', '.join(names)}")
        summary_all = "\n".join(summary)
        return f"Current rating status:\n```{summary_all}```"

    @commands.command(help="Encode the string after the command with the rot-13 scheme.")
    async def rot13(self, ctx, *args):
        reply = None
        if len(args) == 0:
            reply = TextColor.red("Error No text to rotate given as argument to this command.")
        else:
            text = " ".join(args)
            textrot = codecs.encode(text, "rot_13")
            reply = "*rot13 of that is:*\n{:s}".format(textrot)
        await ctx.send(reply)

    @commands.command(help="Rate how good you feel in a scale [1-10] 10 being best. Your rating is valid for 24h.")
    async def rate(self, ctx, rating: int):
        reply = ""
        if rating < 1 or rating > 10:
            reply = TextColor.red("You can only be in states [1, 10].")
        else:
            if rating == 10 and "fredrik" not in ctx.message.author.name.lower():
                rating = 9
                reply = TextColor.red("Sorry; a rating of 10 is reserved for Fredrik. I've downgraded you to a 9.")
            rating_entry = RatingEntry(ctx.message.author, rating)
            self.ratings[ctx.message.author.id] = rating_entry
            # For testing with single user.
            # self.ratings[str(ctx.message.author.id) + str(datetime.now())] = rating_entry
            reply += f":star: Thank you {ctx.message.author.name} for sharing your current rating!\n\n"
            reply += self._rating_status()
        await ctx.send(reply)

    @commands.command(name="rate-status", help="Get current !rate'ings.")
    async def rate_status(self, ctx):
        await ctx.send(self._rating_status())

    @commands.command(name="rate-all", help="Prompt everyone that it's time to !rate")
    async def rate_all(self, ctx):
        reply = "@everyone it's time to `!rate` now!"
        await ctx.send(reply)
