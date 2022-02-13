from discord.ext import commands


class TardsquadClient(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, command_prefix="!", **kwargs)
