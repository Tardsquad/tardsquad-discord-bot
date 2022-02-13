import urllib

from discord.ext import commands

from tardsquad_discord_bot.cog import TardBotCog


class TardBotSearchCommands(TardBotCog, name="Search"):
    @staticmethod
    def search_query(url_fmt, *args):
        query = urllib.parse.quote(" ".join(args))
        url_fmt = "<" + url_fmt + ">"
        return url_fmt.format(query)

    @commands.command(name="google", aliases=["g", "lmgtfy"], help="Search on Google for given query string.")
    async def search_google(self, ctx, *args):
        url_fmt = "https://www.google.com/search?hl=en&q={:s}"
        await ctx.send(TardBotSearchCommands.search_query(url_fmt, *args))

    @commands.command(name="duck", aliases=["d"], help="Search on DuckDuckGo for given query string.")
    async def search_duckduckgo(self, ctx, *args):
        url_fmt = "https://duckduckgo.com/?q={:s}"
        await ctx.send(TardBotSearchCommands.search_query(url_fmt, *args))

    @commands.command(name="youtube", aliases=["y", "yt"], help="Search on YouTube for given query string.")
    async def search_youtube(self, ctx, *args):
        url_fmt = "https://www.youtube.com/results?search_query={:s}"
        await ctx.send(TardBotSearchCommands.search_query(url_fmt, *args))

    @commands.command(name="wikipedia", aliases=["w"], help="Search on Wikipedia for given query string.")
    async def search_wikipedia(self, ctx, *args):
        url_fmt = "http://en.wikipedia.org/wiki/Special:Search?search={:s}"
        await ctx.send(TardBotSearchCommands.search_query(url_fmt, *args))

    @commands.command(name="imdb", aliases=["i"], help="Search on IMDB for given query string.")
    async def search_imdb(self, ctx, *args):
        url_fmt = "https://www.imdb.com/find?q={:s}"
        await ctx.send(TardBotSearchCommands.search_query(url_fmt, *args))
