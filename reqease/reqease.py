import urllib.request
import ssl
import certifi
from dataclasses import dataclass

@dataclass
class Response:
    status_code:int
    headers:list
    body:str

def get(url:str) -> Response:
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url=url, context=context) as response:
        response_object = Response(response.getcode(),
                                   response.getheaders(),
                                   response.read().decode('utf-8'))
    return response_object

def main():
    response = get("https://www.swimplify.co")
    print(response.headers)
    for heade in response.headers:
        print(heade)

if "__main__" == __name__:
    main()