import datetime
from DB.Update import Update

import discord
from discord.ext import commands
from discord.commands import slash_command

class Avatar(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(
        name="avatar",
        name_localizations={"de": "avatar", "en-GB": "avatar"},
        description="Shows the avatar of a member",
        description_localizations={"de": "Zeigt den Avatar von einem Mitglied", "en-GB": "Shows the avatar of a member"})
    @discord.option(
        name="member",
        name_localizations={"de": "mitglied", "en-GB": "member"},
        description="Select a member",
        description_localizations={"de": "Wähle ein Mitglied aus", "en-GB": "Select a member"},
        required=False)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def avatar(self, ctx: discord.ApplicationContext, member: discord.Member):
        """

        Einfacher Discord Avatar Command

        """
        update: tuple = await Update(ctx=ctx, name="Avatar")
        match update[0]:
            case True:
                await ctx.respond(update[1])
            case False:
                if member == None:
                    member = ctx.author
                embed = discord.Embed(title=f"{member.name}'s Avatar", timestamp=datetime.datetime.now(), color=member.color)
                embed.set_footer(text="Developed by Koschinsky")
                embed.set_image(url=member.display_avatar.url)
                await ctx.respond(embed=embed)

def setup(client: commands.Bot):
    client.add_cog(Avatar(client))