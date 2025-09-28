from discord.ext import commands
from config import TOKEN, INTENTS

class Bot(commands.Bot):
    async def setup_hook(self):
        for ext in ["scheduler"]:
            try:
                await self.load_extension(ext)
                print(f"Loaded extension: {ext}")
            except Exception as e:
                print(f"Failed to load extension {ext}: {e}")

bot = Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
        
if __name__ == "__main__":
    bot.run(TOKEN)