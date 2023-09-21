import discord
from discord.ext import commands

class Error_handler(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error):
        match error:
            case error if isinstance(error, commands.CommandOnCooldown):
                responses: dict = {
                    "de": f"Versuch es nochmal nach {error.retry_after:.0f} Sekunden",
                    "en-GB": f"Try again after {error.retry_after:.0f} seconds"}
                await ctx.respond(responses.get(ctx.interaction.locale, responses["en-GB"]))

def setup(client: commands.Bot):
    client.add_cog(Error_handler(client))