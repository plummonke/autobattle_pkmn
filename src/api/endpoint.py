from typing import Dict

class Endpoint:
    def __init__(self, url: str, endpoint_data: Dict):
        self.base_url = url
        self.name = endpoint_data['name']
        self.endpoint = f'{url}/{self.name}'

    def get_data(self, id: str | int) -> Dict:
        req = Request(self.format_url(id))
        return json.loads(self.send_request(req))

    def format_url(self, id: str | int) -> str:
        return f'{self.endpoint}/{id}'

    def send_request(self, req: Request) -> bytes:
        try:
            response = urlopen(req)
            return response.read()
        except HTTPError as e:
            raise EndpointRequestError(self.name, e.code)
