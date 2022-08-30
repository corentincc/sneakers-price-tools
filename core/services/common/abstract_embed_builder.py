import abc

from discord import Embed


class AbstractEmbedBuilderService(abc.ABC):
    @staticmethod
    async def build_sneakers_embed(sneakers) -> Embed:
        pass

    @staticmethod
    async def build_prices_embed(sneaker, prices) -> Embed:
        pass
