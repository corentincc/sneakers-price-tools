import os
import random

from dotenv import load_dotenv

from config import ROOT_DIR
from core.models.proxy import Proxy
from core.utils.bprint import PrintUtils


class ProxyService:
    is_init = False
    _filename = None
    _proxies = []

    @classmethod
    def init(cls):
        cls._filename = os.getenv("PROXY_FILENAME")
        if cls._filename == "":
            return

        PrintUtils.print_with_date_info("Initializing ProxyService")

        load_dotenv()

        try:
            with open(f"{ROOT_DIR}/{cls._filename}") as proxy_file:
                if lines := proxy_file.readlines():
                    try:
                        for proxy in lines:
                            split_proxy = proxy.split(":")
                            cls._proxies.append(
                                Proxy.parse_obj(
                                    {
                                        "http": f"http://{split_proxy[2]}:{split_proxy[3].strip()}@{split_proxy[0]}:{split_proxy[1]}",
                                        "https": f"https://{split_proxy[2]}:{split_proxy[3].strip()}@{split_proxy[0]}:{split_proxy[1]}",
                                    }
                                )
                            )
                        cls.is_init = True
                    except Exception:  # This is bad 🤡
                        cls.is_init = False
                        PrintUtils.print_with_date_warning(
                            "Failed to init ProxyService, check the format"
                        )

                else:
                    cls.is_init = False
                    PrintUtils.print_with_date_warning(f"{cls._filename} is empty")
        except FileNotFoundError:
            cls.is_init = False
            PrintUtils.print_with_date_error(f"Can't find {cls._filename}")

    @classmethod
    def get_proxy(cls) -> Proxy:
        if cls.is_init:
            return random.choice(cls._proxies)
