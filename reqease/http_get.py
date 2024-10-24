import urllib.request
import ssl
import certifi
from dataclasses import dataclass
import json

@dataclass
class Response:
    status_code:int
    headers:list
    body_bytes: bytes
    body_str:str

def get(url:str) -> Response:
    """Retrieves content from the specified URL over HTTPS and returns a Response object.

    Args:
        url (str): The URL to fetch data from. Must be a valid HTTPS URL.

    Returns:
        Response(object): A custom Response object with the following attributes:
        status_code (int): The HTTP status code from the server (e.g., 200, 404).
        headers (list[tuple]): A list of headers (key-value pairs) from the server response.
        body_bytes (bytes): The raw body content of the response in bytes.
        body_str (str): The body content of the response decoded as a UTF-8 string.
    """
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url=url, context=context) as response:
        body_bytes = response.read()
        return Response(status_code = response.getcode(),
                        headers = response.getheaders(),
                        body_bytes = body_bytes,
                        body_str = body_bytes.decode('utf-8'))

def to_file(url:str, file_path:str) -> None:
    """Fetches data from the given URL and writes it to a specified file.

    Args:
        url (str): The URL to fetch data from. Must be a valid HTTPS URL.
        file_path (str): The path where the content will be saved. The file will be created if it does not exist, and its contents will be overwritten.

    Returns:
        None: This function does not return a value.
    """
    response = get(url)
    with open(file_path,'w') as file:
        file.write(response.body_str)

def to_json(url:str) -> object:
    """Fetches JSON data from the given URL and returns it as a Python object.

    Args:
        url (str): The URL to fetch data from. Must be a valid HTTPS URL containing JSON data.

    Returns:
        dict or list: The JSON content parsed as a Python dictionary or list, depending on the structure of the JSON response.
    """
    response = get(url)
    json_object = json.loads(response.body_str)
    return json_object