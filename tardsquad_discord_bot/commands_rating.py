import shelve
from operator import attrgetter

from discord.ext import commands

import tardsquad_discord_bot
from tardsquad_discord_bot.cog import TardBotCog
from tardsquad_discord_bot.ratingentry import RATING_EXPIRES_AFTER_H, RatingEntry
from tardsquad_discord_bot.textcolor import TextColor


class TardBotRatingCommands(TardBotCog, name="Rating"):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ratings = shelve.open("./ratings.shelve", flag="c", writeback=True)

    @commands.Cog.listener()
    async def on_disconnect(self):
        # We don't modify the RatingEntry outside of the shelve operations, so this should not be needed. But just in case...
        self.ratings.sync()

    def _rating_gc(self):
        for author_id in list(self.ratings):
            if self.ratings[author_id].expired():
                del self.ratings[author_id]

    def _rating_status(self):
        self._rating_gc()
        if not self.ratings:
            return "*Currently no active ratings collected*\n\nPlease share your rating with the `!rate` command."
        summary = []
        for entry in reversed(sorted(self.ratings.values(), key=attrgetter("rating"))):
            reason = f": {entry.reason}" if entry.reason else ""
            summary.append(f"* {entry.rating} @{entry.username} [expires in {entry.expires_at()}]{reason}")
        summary_all = "\n".join(summary)
        return f"Current rating status:\n```{summary_all}```"

    @commands.command(
        help=f"Rate how good you feel on a scale [1-10], with 10 being best.\nYour rating is valid for {RATING_EXPIRES_AFTER_H}h.\nAn optional reason can also be given (must be a double-quoted string!)."
    )
    async def rate(self, ctx, rating: int, reason=None):
        reply = ""
        if rating < 1 or rating > 10:
            reply = TextColor.red("You can only be in states [1, 10].")
        else:
            if rating == 10 and "fredrik" not in ctx.message.author.name.lower():
                rating = 9
                reply = TextColor.red("Sorry; a rating of 10 is reserved for Fredrik. I've downgraded you to a 9.")
            rating_entry = RatingEntry(ctx.message.author.name, rating, reason)
            self.ratings[str(ctx.message.author.id)] = rating_entry
            # For testing with single user.
            # self.ratings[str(ctx.message.author.id) + str(__import__("datetime").datetime.now())] = rating_entry
            reply += f":star: Thank you {ctx.message.author.name} for sharing your current rating!\n\n"
            reply += self._rating_status()
        await ctx.send(reply)

    @commands.command(name="rate-status", help="Get current !rate'ings.")
    async def rate_status(self, ctx):
        await ctx.send(self._rating_status())

    @commands.command(name="rate-standup", help="Prompt everyone that it's time to !rate")
    async def rate_standup(self, ctx):
        reply = "@everyone it's time to `!rate` now!"
        await ctx.send(reply)
