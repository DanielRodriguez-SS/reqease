import urllib.request
import urllib.parse
import ssl
import certifi
import json
from dataclasses import dataclass

@dataclass
class Response:
    status_code:int
    headers:list
    body_bytes: bytes
    body_str:str

def post(url: str, data: dict, headers: dict | None = None) -> Response:

    # Encode the data as bytes
    if "Content-Type" in headers.keys():
        if headers['Content-Type'] == "application/json":
            encoded_data = json.dumps(data).encode("utf-8")
    else:
        encoded_data = urllib.parse.urlencode(data).encode("utf-8")

    # Create a Request object
    request = urllib.request.Request(url, data=encoded_data, method='POST')

    # Add headers to the request if provided
    if headers:
        for key, value in headers.items():
            request.add_header(key, value)

    # Create a secure SSL context    
    context = ssl.create_default_context(cafile=certifi.where())

    # Send the request and retreive response
    with urllib.request.urlopen(request, context=context) as response:
        body_bytes = response.read()
        return Response(status_code= response.getcode(),
                        headers= response.getheaders(), 
                        body_bytes= body_bytes, 
                        body_str= body_bytes.decode('utf-8'))



products = [{"productType":"RIMS","productId":"100253285","quantity":1},
             {"productType":"RIMS","productId":"100253284","quantity":1}]

data = {"correlationId":"5f8404f6-7606-44dc-979f-fb562d3323b4","data":{"isExplore":True,"lineOfBusiness":"035","products":products}}
headers = {"ConsumerId":"0KhnFrg3bhvNW38ofwPGVMHoR2luZUlG",
          "Content-Type": "application/json"}

res = post(url="https://tapi.telstra.com/v1/logistics/ext/stock-check", data=data, headers=headers)
print(res.status_code)
print(res.body_str)