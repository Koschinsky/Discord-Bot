import asyncio
from DB.Update import Update

import discord
from discord.ext import commands
from discord.commands import slash_command

class Shutdown(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    #def is_guild_owner():
    #    def predicate(ctx: discord.ApplicationContext):
    #        with open("DB/Config.json", "r") as f:
    #            data = json.load(f)
    #        return ctx.guild is not None and ctx.author.id in data["Server Owner"]
    #    return commands.check(predicate)
    """
    
    Permission check, damit nicht jeder auf dem Server den Command benutzen kann

    """

    @slash_command(
        name="shutdown",
        name_localizations={"de": "herunterfahren", "en-GB": "shutdown"},
        description="Shuts down the bot",
        description_localizations={"de": "Fährt den Bot herunter", "en-GB": "Shut down the bot"})
    #@commands.check_any(commands.is_owner(), is_guild_owner())
    async def shutdown(self, ctx: discord.ApplicationContext):
        """
        
        Einfacher Shutdown command
        
        """
        update = await Update(ctx=ctx, name="Shutdown")
        print(update)
        match update[0]:
            case True:
                await ctx.respond(update[1])
            case False:
                responses: dict = {
                    "de": "Möchtest du wirklich den Bot herunterfahren? (Ja/Nein)",
                    "en-GB": "Do you really want to shutdown the bot? (Yes/No)"}
                await ctx.respond(responses.get(ctx.interaction.locale, responses["en-GB"]))
                message: discord.Message = await self.client.wait_for("message", check=lambda message: message.author == ctx.author)
                msg = message.content.lower().replace(" ", "")
                match msg:
                    case msg if msg in ["yes", "ja"]:
                        responses: dict = {
                            "de": "auf Wiedersehen",
                            "en-GB": "Bye"}
                        await ctx.respond(responses.get(ctx.interaction.locale, responses["en-GB"]))
                        await asyncio.sleep(5)
                        await self.client.close()
                    case msg if msg in ["no", "nein"]:
                        responses: dict = {
                            "de": "Ich werde mich nicht herunter fahren",
                            "en-GB": "Im not shutting down"}
                        await ctx.respond(responses.get(ctx.interaction.locale, responses["en-GB"]))

def setup(client: commands.Bot):
    client.add_cog(Shutdown(client))