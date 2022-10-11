from pydantic import BaseModel


class Proxy(BaseModel):
    http: str
    https: str
