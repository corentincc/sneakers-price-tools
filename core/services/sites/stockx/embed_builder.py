from datetime import datetime, timezone

from discord import Embed

from core.services.common.abstract_embed_builder import AbstractEmbedBuilderService


class StockxEmbedBuilderService(AbstractEmbedBuilderService):
    @staticmethod
    async def build_sneakers_embed(sneakers) -> Embed:
        text_field1 = ""
        text_field2 = ""

        for i, sneaker in enumerate(sneakers):
            text_field1 += f"{i}\n"
            text_field2 += (
                f"{sneaker.get('title')} - {sneaker.get('traits')[0].get('value')}\n"
            )

        embed = Embed(
            title="Select a sneaker",
            timestamp=datetime.now(timezone.utc),
        )

        embed.add_field(name="id 🪪", value=text_field1, inline=True)
        embed.add_field(name="Sneaker 👟", value=text_field2, inline=True)
        embed.set_footer(text="Stockx - SneakersPriceTool")
        return embed

    @staticmethod
    async def build_prices_embed(sneaker, prices) -> Embed:
        text_field1 = ""
        text_field2 = ""

        for price in prices:
            text_field1 += f"{price.get('size')}\n"
            text_field2 += f"{price.get('price')}\n"

        embed = Embed(
            title=sneaker.get("title"),
            url=f"https://www.stockx.com/{sneaker.get('urlKey')}",
            timestamp=datetime.now(timezone.utc),
        )

        embed.set_thumbnail(url=sneaker.get("media").get("imageUrl"))
        embed.add_field(name="Size 👟", value=text_field1, inline=True)
        embed.add_field(name="Payouts 💸", value=text_field2, inline=True)
        embed.set_footer(text="Stockx - SneakersPriceTool")
        return embed
