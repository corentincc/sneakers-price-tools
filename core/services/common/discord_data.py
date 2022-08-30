import os

from dotenv import load_dotenv

from core.utils.bprint import PrintUtils


class DiscordDataService:

    _discord_data = {
        "discord_token": None,
    }

    @classmethod
    def get_discord_data(cls):
        cls._check_is_init()
        return cls._discord_data

    @classmethod
    def init(cls):
        PrintUtils.print_with_date_info("Initializing DiscordDataService")

        load_dotenv()

        cls._discord_data["discord_token"] = os.getenv("DISCORD_TOKEN")
        try:
            cls._check_is_init()
        except RuntimeError:
            PrintUtils.print_with_date_error("Failed to init DiscordDataService")
            quit()

    @classmethod
    def _check_is_init(cls):
        """
        Check if service is initialized and raise RuntimeError if not
        """
        if cls._discord_data.get("discord_token") is None:
            raise RuntimeError("DiscordDataService not initialized")
