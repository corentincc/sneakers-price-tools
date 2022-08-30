import os
from dotenv import load_dotenv

from core.utils.bprint import PrintUtils


class RestocksUserService:

    _user = {
        "email": None,
        "password": None,
    }

    @classmethod
    def get_user(cls):
        cls._check_is_init()
        return cls._user

    @classmethod
    def init(cls):
        PrintUtils.print_with_date_info("Initializing RestocksUserService")

        load_dotenv()

        cls._user["email"] = os.getenv("RESTOCKS_EMAIL")
        cls._user["password"] = os.getenv("RESTOCKS_PASSWORD")
        try:
            cls._check_is_init()
        except RuntimeError:
            PrintUtils.print_with_date_error("Failed to init UserService")
            quit()

    @classmethod
    def _check_is_init(cls):
        """
        Check if service is initialized and raise RuntimeError if not
        """
        if cls._user.get("email") is None or cls._user.get("password") is None:
            raise RuntimeError("UserService not initialized")
