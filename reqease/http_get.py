import urllib.request
import ssl
import certifi
from data_classes import Response
from response_processor import ResponseProcessor

class Get(ResponseProcessor):
    def __init__(self, url: str, headers: dict | None = None) -> None:
        self.url = url
        self.headers = headers
        self.response = self._make_request()

    def _make_request(self) -> Response:
        # Create a Request object
        request = urllib.request.Request(self.url)

        # Add headers to the request if provided
        if self.headers:
            for key, value in self.headers.items():
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