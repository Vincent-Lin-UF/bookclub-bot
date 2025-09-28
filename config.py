import os
import discord
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))
ROLE_ID = int(os.getenv("ROLE_ID", "0"))

TZ = ZoneInfo("America/New_York")
INTENTS = discord.Intents.default()
ALLOWED_MENTIONS = discord.AllowedMentions(roles=True)
