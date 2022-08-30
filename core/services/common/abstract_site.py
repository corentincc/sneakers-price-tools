import abc


class AbstractSiteService(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    async def search(sku) -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    async def get_prices(sneaker_id) -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_id(sneaker: dict) -> str:
        pass
