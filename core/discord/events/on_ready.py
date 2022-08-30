from core.discord.bot import Bot
from core.utils.bprint import PrintUtils

client = Bot().client


@client.event
async def on_ready():
    PrintUtils.print_with_date_success(f"Bot launched [{client.user}]")
