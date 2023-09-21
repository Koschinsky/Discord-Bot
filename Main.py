import json
import traceback
from DB.Token import Token, New_token

import discord
from discord.ext import commands

with open("DB/Config.json", "r") as f:
    data = json.load(f)

client: commands.Bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(">>"),
    strip_after_prefix=True,
    case_insensitive=True,
    intents=discord.Intents.all(),
    auto_sync_commands=True,
    help_command=None,
    #owner_ids=data["Bot Owner"] #Für Botowner only commands
    )

try:
    client.load_extension("Cogs", recursive=True)
except Exception:
    print(traceback.format_exc())

if __name__ == "__main__":
    try:
        client.run(Token())
    except Exception:
        New_token()