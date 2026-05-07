from typing import Dict

class Endpoint:
    def __init__(self, url: str, endpoint_data: Dict):
        self.base_url = url
        self.endpoint = f'{url}/{endpoint_data["name"]}'

    def format_url(self, id: str | int) -> str:
        return f'{self.endpoint}/{id}'
