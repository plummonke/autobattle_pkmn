import json

class Config:
    def __init__(self, filename: str):
        self.filename = filename
        data = json.load(filename)

        self.api_base_url = data['base_url']
        self.endpoint_filename = data['endpoint_file']
        self.cache_filename = data['cache']

    def get_ep_filename(self) -> str:
        return self.endpoint_filename

    def get_api_base_url(self) -> str:
        return self.api_base_url

    def get_cache_filename(self) -> str:
        return self.cache_filename
