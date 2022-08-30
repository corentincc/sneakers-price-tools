import re

import requests

from core.services.sites.restocks.user import RestocksUserService
from core.utils.bprint import PrintUtils


class RestocksAuthService:

    _auth_token = None
    _restocks_language = None

    @classmethod
    def get_auth_token(cls):
        return cls._auth_token

    @classmethod
    def get_restocks_language(cls):
        return cls._restocks_language

    @classmethod
    def init(cls):
        PrintUtils.print_with_date_info("Initializing RestocksAuthService")
        cls._restocks_language = cls.gen_restocks_language()
        cls._auth_token = cls.gen_auth_token()
        try:
            cls._check_is_init()
        except RuntimeError:
            PrintUtils.print_with_date_error("Failed to init AuthService")
            quit()

    @classmethod
    def _check_is_init(cls):
        """
        Check if service is initialized and raise RuntimeError if not
        """
        if (
            cls._auth_token is None
            or cls._restocks_language is None
            or not cls.check_auth_token()
        ):
            raise RuntimeError("AuthService not initialized")

    @classmethod
    def build_cookies(cls, session):
        s = "".join(f"{k}={v}; " for k, v in dict(session.cookies).items())
        s = s[:-2]
        return s

    @staticmethod
    def gen_restocks_language():
        response = requests.get(
            "https://restocks.net/",
        )

        return response.url.split("/")[-1]

    @classmethod
    def check_auth_token(cls):
        cookies = {"restocks_session": cls.get_auth_token()}

        response = requests.get(
            f"https://restocks.net/{cls._restocks_language}/account",
            cookies=cookies,
        )

        return response.url == f"https://restocks.net/{cls._restocks_language}/account"

    @classmethod
    def gen_auth_token(cls):

        session = requests.session()

        # csrf_token gen
        response = session.get(f"https://restocks.net/{cls._restocks_language}/login")
        csrf_token = re.search(
            '(?<=<meta name="csrf-token" content=")(.*)(?=">)', response.text
        )[1]

        _user = RestocksUserService.get_user()

        # authenticated restocks_session gen
        headers = {
            "cookies": cls.build_cookies(session),
        }

        data = {
            "_token": csrf_token,
            "email": _user.get("email"),
            "password": _user.get("password"),
        }

        response = session.post(
            f"https://restocks.net/{cls._restocks_language}/login",
            headers=headers,
            data=data,
        )

        return response.cookies.get("restocks_session")
