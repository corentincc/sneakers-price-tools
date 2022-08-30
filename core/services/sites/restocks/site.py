import requests

from core.services.common.abstract_site import AbstractSiteService
from core.services.sites.restocks.auth import RestocksAuthService
from core.utils.bprint import PrintUtils


class RestocksSiteService(AbstractSiteService):
    @staticmethod
    async def search(sku) -> list:
        params = {
            "q": sku,
            "page": "1",
        }

        response = requests.get(
            f"https://restocks.net/{RestocksAuthService.get_restocks_language()}/shop/search",
            params=params,
        )

        return response.json().get("data")[:5]

    @staticmethod
    async def get_prices(sneaker) -> list:
        if not RestocksAuthService.check_auth_token():
            PrintUtils.print_with_date_warning("auth_token expired")
            RestocksAuthService.init()

        response = requests.get(
            f"https://restocks.net/{RestocksAuthService.get_restocks_language()}/product/get-sizes/{sneaker.get('id')}"
        )

        cookies = {"restocks_session": RestocksAuthService.get_auth_token()}

        prices = []

        for sizes in response.json():
            sizes_price = requests.get(
                f"https://restocks.net/{RestocksAuthService.get_restocks_language()}/product/get-lowest-price/{sneaker.get('id')}/{sizes.get('id')}",
                cookies=cookies,
            )
            if sizes_price.json() == 0:
                prices.append(
                    {"size": sizes.get("name"), "price": "Be the first to list !"}
                )
            else:
                sizes_price = int(int(sizes_price.json()) * 0.9) - 10
                prices.append({"size": sizes.get("name"), "price": f"{sizes_price}€"})

        return prices
