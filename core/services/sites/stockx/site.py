import math

from core.services.common.abstract_site import AbstractSiteService
from core.services.common.client import ClientService


class StockxSiteService(AbstractSiteService):
    @staticmethod
    async def search(sku) -> list:
        params = {
            "_search": sku,
            "dataType": "product",
        }

        s = ClientService.get_session()

        response = s.get("https://stockx.com/api/browse", params=params)

        return response.json().get("Products")[:5]

    @staticmethod
    async def get_prices(sneaker) -> list:
        s = ClientService.get_session()

        response = s.get(
            f"https://stockx.com/api/products/{sneaker.get('id')}?includes=market,360&currency=EUR&market=FR&country=FR",
        )

        prices = []

        for product in response.json().get("Product").get("children").values():
            price = math.floor(
                (int(product.get("market").get("highestBid")) * 0.875) - 5
            )
            prices.append(
                {
                    "size": product.get("market").get("highestBidSize"),
                    "price": f"{price}€",
                }
            )

        return prices
