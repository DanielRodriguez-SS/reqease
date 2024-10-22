import urllib.request
import ssl
import json
import certifi

context = ssl.create_default_context(cafile=certifi.where())
with urllib.request.urlopen('https://www.swimplify.co/projects/andromeda-api.json', context=context) as response:
    content = response.read()

data = content.decode('utf-8')
json_data = json.loads(data)
print(data)

with open('html3.txt', 'w') as file:
    file.write(data)