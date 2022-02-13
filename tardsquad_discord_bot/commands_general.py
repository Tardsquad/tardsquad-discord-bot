import codecs

from discord.ext import commands

from tardsquad_discord_bot.cog import TardBotCog
from tardsquad_discord_bot.textcolor import TextColor


# TODO add a "!weather <location>" command?
class TardBotGeneralCommands(TardBotCog, name="General"):
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
