import math

import requests

from core.services.common.abstract_site import AbstractSiteService


class StockxSiteService(AbstractSiteService):
    @staticmethod
    async def search(sku) -> list:
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83",
        }

        params = {
            "_search": sku,
            "dataType": "product",
        }

        response = requests.get(
            "https://stockx.com/api/browse", params=params, headers=headers
        )

        return response.json().get("Products")[:5]

    @staticmethod
    async def get_prices(sneaker_id) -> list:
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83",
        }

        response = requests.get(
            f"https://stockx.com/api/products/{sneaker_id}?includes=market,360&currency=EUR&market=FR&country=FR",
            headers=headers,
        )

        prices = []

        for product in response.json()["Product"]["children"].values():
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

    @staticmethod
    def get_id(sneaker: dict) -> str:
        return sneaker.get("id")
