from typing import Protocol
from data_classes import Response

class ResponseProtocol(Protocol):
    url: str
    response: Response