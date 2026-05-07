from typing import Dict

class Endpoint:
    def __init__(self, url: str, endpoint_data: Dict):
        self.base_url = url
        self.endpoint = f'{url}/{endpoint_data["name"]}'

    def get_data(self, id: str | int) -> Dict:
        req = Request(self.format_url(id))
        return json.loads(self.send_request(req))

    def format_url(self, id: str | int) -> str:
        return f'{self.endpoint}/{id}'

    def send_request(self, req: Request) -> bytes:
        response = urlopen(req)
        return response.read()
