* Bump discord.py to 2.0
  * https://pypi.org/project/discord.py/#history
  * https://discordpy.readthedocs.io/en/latest/migrating.html
* Switch to slash commands
  * https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ
* `!rate <nbr>` should useuse built-in range check
  * Replace https://github.com/Tardsquad/tardsquad-discord-bot/blob/d6b6399d8e3ccc74cde764b9d053299cc045a708/tardsquad_discord_bot/commands_rating.py#L46 with `app_commands.Range[int, 1, 10]`
  * https://gist.github.com/Rapptz/c4324f17a80c94776832430007ad40e6#range
