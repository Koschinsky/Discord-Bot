from DB.Update import Update

import discord
from discord.ext import commands
from discord.commands import slash_command

class Ping(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(
        name="ping",
        name_localizations={"de": "ping", "en-GB": "ping"},
        description="Shows the ping of the bot",
        description_localizations={"de": "Zeigt den Ping von dem Bot", "en-GB": "Shows the ping of the bot"})
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def ping(self, ctx: discord.ApplicationContext):
        """

        Einfacher Ping Command

        """
        update: tuple = await Update(ctx=ctx, name="Ping")
        match update[0]:
            case True:
                await ctx.respond(update[1])
            case False:
                responses = {
                    "de": f"Latenz ist {round(self.client.latency * 1000)} ms",
                    "en-GB": f"Latency is {round(self.client.latency * 1000)} ms"}
                await ctx.respond(responses.get(ctx.interaction.locale, responses["en-GB"]))

def setup(client: commands.Bot):
    client.add_cog(Ping(client))