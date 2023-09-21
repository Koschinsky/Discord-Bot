import json

import discord

async def Data(key: str):
    with open("DB/Config.json", "r") as f:
        data = json.load(f)
    return data["Commands"][key]

async def Update(ctx: discord.ApplicationContext, name: str):
    data = await Data(key=name)
    match data:
        case 1:
            responses = {
                "de": "Der Command ist derzeit nicht verfügbar",
                "en-GB": "The command is not currently available"}
            return (True, responses.get(ctx.interaction.locale, responses["en-GB"]))
        case 0:
            return (False, False)