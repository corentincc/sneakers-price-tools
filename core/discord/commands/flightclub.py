from discord_slash.utils.manage_commands import create_option

from core.discord.bot import Bot
from core.discord.utils.site import DiscordSiteUtils
from core.services.sites.flightclub.embed_builder import FlightClubEmbedBuilderService
from core.services.sites.flightclub.site import FlightClubSiteService


bot = Bot()


@bot.slash_client.slash(
    name="fc",
    description="Get flightclub prices of a sku",
    options=[
        create_option(
            name="sku", description="Sneaker sku", option_type=3, required=True
        )
    ],
)
async def prices(ctx, sku: str):
    discord_site_utils = DiscordSiteUtils(ctx)
    await discord_site_utils.prices(
        sku, bot, FlightClubSiteService, FlightClubEmbedBuilderService
    )
