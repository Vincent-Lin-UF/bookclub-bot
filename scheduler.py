from datetime import datetime, time, date
from discord.ext import tasks, commands
from config import TZ, CHANNEL_ID, ROLE_ID, ALLOWED_MENTIONS

REMINDER_TEXT = "to read :)"
ANCHOR_DATE = date.today()

class Scheduler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.every_other_day_tick.start()

    def cog_unload(self):
        self.every_other_day_tick.cancel()

    @tasks.loop(time=time(18, 8, tzinfo=TZ))
    async def every_other_day_tick(self):
        today = datetime.now(TZ).date()
        if CHANNEL_ID and ROLE_ID and (today - ANCHOR_DATE).days % 2 == 0:
            channel = self.bot.get_channel(CHANNEL_ID) or await self.bot.fetch_channel(CHANNEL_ID)
            message = f"<@&{ROLE_ID}> {REMINDER_TEXT}"
            await channel.send(message, allowed_mentions=ALLOWED_MENTIONS)

    @every_other_day_tick.before_loop
    async def before_tick(self):
        await self.bot.wait_until_ready()
        
async def setup(bot):
    await bot.add_cog(Scheduler(bot))