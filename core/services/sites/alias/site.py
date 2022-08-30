import math

import requests

from core.services.common.abstract_site import AbstractSiteService


class AliasSiteService(AbstractSiteService):
    @staticmethod
    async def search(sku) -> list:

        headers = {
            "X-Algolia-Application-Id": "2FWOTDVM2O",
            "X-Algolia-API-Key": "838ecd564b6aedc176ff73b67087ff43",
            "User-Agent": "Algolia for Android (3.27.0); Android (11)",
            "Content-type": "application/json; charset=UTF-8",
            "Connection": "Keep-Alive",
        }

        json_data = {
            "params": f"analyticsTags=%5B%22platform%3Aandroid%22%2C%22channel%3Aalias%22%5D&distinct=true&facets=%5B%22product_type%22%5D&filters=&hitsPerPage=20&page=0&query={sku}",
        }

        response = requests.post(
            "https://2fwotdvm2o-dsn.algolia.net/1/indexes/product_variants_v2/query",
            headers=headers,
            json=json_data,
        )

        return response.json().get("hits")[:5]

    @staticmethod
    async def get_prices(sneaker) -> list:

        prices = []

        for size in sneaker.get("size_range"):
            json_data = {
                "variant": {
                    "consigned": False,
                    "id": sneaker.get("slug"),
                    "packaging_condition": "PACKAGING_CONDITION_GOOD_CONDITION",
                    "product_condition": "PRODUCT_CONDITION_NEW",
                    "region_id": 2,
                    "size": size,
                },
            }
            response = requests.post(
                "https://sell-api.goat.com/api/v1/analytics/variants/availability",
                json=json_data,
            )

            price = response.json().get("lowest_price_cents")
            if price is None:
                prices.append({"size": size, "price": "Be the first to list !"})
            else:
                price = math.floor((int(price) * 0.876 - 6) * 0.01)
                prices.append(
                    {
                        "size": size,
                        "price": f"{price}€",
                    }
                )

        return prices
