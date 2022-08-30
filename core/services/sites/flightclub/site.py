import math

import requests

from core.services.common.abstract_site import AbstractSiteService


class FlightClubSiteService(AbstractSiteService):
    @staticmethod
    async def search(sku) -> list:
        params = {
            "query": sku,
        }

        response = requests.get(
            "https://sell.flightclub.com/api/public/search", params=params
        )

        return response.json().get("results")[:5]

    @staticmethod
    async def get_prices(sneaker_id) -> list:

        response = requests.get(
            f"https://sell.flightclub.com/api/public/products/{sneaker_id}",
        )

        prices = []

        for size, price in response.json()["suggestedPrices"].items():
            if price.get("lowestConsignedPriceCents"):
                price = int(price.get("lowestConsignedPriceCents"))
            else:
                price = int(price.get("highestPriceMark"))
            price = math.floor((price * 0.876 - 5) * 0.01)
            if price == 5146:
                prices.append({"size": size, "price": "--"})
            else:
                prices.append(
                    {
                        "size": size,
                        "price": f"{price}€",
                    }
                )

        return prices

    @staticmethod
    def get_id(sneaker: dict) -> str:
        return sneaker.get("id")
