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

def get(url: str, headers: dict | None = None) -> Response:
    """Sends an HTTPS GET request to the specified URL and returns a custom Response object.

    Args:
        url (str): The URL to send the GET request to. Must be a valid HTTPS URL.
        headers (dict | None): Optional dictionary of HTTP headers to include in the request.

    Returns:
        Response: A custom Response object with the following attributes:
            - status_code (int): The HTTP status code from the server (e.g., 200, 404).
            - headers (list[tuple]): A list of headers (key-value pairs) from the server response.
            - body_bytes (bytes): The raw body content of the response in bytes.
            - body_str (str): The body content of the response decoded as a UTF-8 string.
    """
    # Create a Request object
    request = urllib.request.Request(url)
    
    # Add headers to the request if provided
    if headers:
        for key, value in headers.items():
            request.add_header(key, value)

    # Create a secure SSL context    
    context = ssl.create_default_context(cafile=certifi.where())
    
    # Send the reuest and retreive the response
    with urllib.request.urlopen(request, context=context) as response:
        body_bytes = response.read()
        return Response(status_code = response.getcode(),
                        headers = response.getheaders(),
                        body_bytes = body_bytes,
                        body_str = body_bytes.decode('utf-8'))

def to_file(url: str, file_path: str, headers: dict | None = None) -> None:
    """Fetches content from a URL and saves it to a specified file. If the file path ends with '.json',
    the content is saved as a JSON dictionary; otherwise, it is saved as plain text.

    Args:
        url (str): The URL to fetch the content from.
        file_path (str): The path where the content should be saved. If it ends with '.json',
                         the content is parsed as JSON and formatted accordingly.
        headers (dict | None): Optional dictionary of HTTP headers to include in the request.

    Returns:
        None: This function saves the output directly to a file and does not return any value.
    """
    with open(file_path,'w') as file:
        if '.json' in file_path:
            data = to_dict(url, headers)
            json.dump(data, file, indent=4)
        else:
            response = get(url, headers)
            file.write(response.body_str)

def to_dict(url: str, headers: dict | None = None) -> dict:
    """Sends a GET request to the specified URL, parses the response as JSON, and returns it as a dictionary.

    Args:
        url (str): The URL to fetch data from. The response should be in JSON format.
        headers (dict | None): Optional dictionary of HTTP headers to include in the request.

    Returns:
        dict: A dictionary representing the JSON data from the response.

    Raises:
        ValueError: If the response cannot be parsed as a dictionary, indicating that the endpoint did not return valid JSON.
    """
    response = get(url, headers)
    try:
        parsed = json.loads(response.body_str)
        return parsed
    except:
        raise ValueError(f"The endpoint '{url}' is not a valid dictionary format.")