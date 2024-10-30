import json
from protocols import ResponseProtocol

class ResponseProcessor:
    def __init__(self, protocol: ResponseProtocol) -> None:
        self.response = protocol.response
        self.url = protocol.url

    @property
    def to_dict(self) -> dict:
        try:
            return json.loads(self.response.body_str)
        except:
            raise ValueError(f"The endpoint '{self.url}' is not a valid dictionary format.")
        
    def to_file(self, file_path: str) -> None:
        with open(file_path,'w') as file:
            if '.json' in file_path:
                data = self.to_dict
                json.dump(data, file, indent=4)
            else:
                file.write(self.response.body_str)