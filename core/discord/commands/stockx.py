from discord_slash.utils.manage_commands import create_option

from core.discord.bot import Bot
from core.discord.utils.site import DiscordSiteUtils
from core.services.sites.stockx.embed_builder import StocksEmbedBuilderService
from core.services.sites.stockx.site import StockxSiteService


bot = Bot()


@bot.slash_client.slash(
    name="stockx",
    description="Get stockx prices of a sku",
    options=[
        create_option(
            name="sku", description="Sneaker sku", option_type=3, required=True
        )
    ],
)
async def prices(ctx, sku: str):
    discord_site_utils = DiscordSiteUtils(ctx)
    await discord_site_utils.prices(
        sku, bot, StockxSiteService, StocksEmbedBuilderService
    )
