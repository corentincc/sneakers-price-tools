from tls_client import Session

from core.services.common import ProxyService


class ClientService:
    @classmethod
    def get_session(cls) -> Session:
        s = Session(client_identifier="chrome_106")
        if ProxyService.is_init:
            s.proxies.update(ProxyService.get_proxy())
        return s
