from discord.ext import commands
from discord_slash import SlashCommand

from core.services.common import DiscordDataService


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Bot(metaclass=SingletonMeta):

    client = commands.Bot(command_prefix=".restocks")
    slash_client = SlashCommand(client, sync_commands=True)

    def __init__(self):
        self._discord_data = DiscordDataService.get_discord_data()
        from . import commands  # noqa
        from . import events  # noqa

    def run(self):
        self.client.run(self._discord_data.get("discord_token"))
