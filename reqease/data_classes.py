from dataclasses import dataclass

@dataclass
class Response:
    status_code:int
    headers:list
    body_bytes: bytes
    body_str:str