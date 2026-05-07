import json

from typing import Dict
from urllib.error import HTTPError
from urllib.request import Request, urlopen

class Service:
    '''Service manages calls to the PokeAPI.
    '''
    def __init__(self, config_file: str):
        try:
            self.config = Config(config_file)
        except Exception as e:
            raise ServiceInitializationError(str(e))

        try:
            with open(self.config.get_ep_filename(), 'r') as f:
                eps = json.load(f)
                self.endpoints = {k: self.create_endpoint(v) for k, v in eps}
        except Exception as e:
            raise ServiceInitializationError(str(e))

        self.cacher = Cacher(self.config.get_cache_filename())

    def create_endpoint(self, endpoint: Dict):
        return Endpoint(self.config.get_api_base_url(), endpoint)
    
    def request_endpoint(self, endpoint_name: str, id: str | int) -> Dict:
        return self.endpoints[endpoint_name].get_data(id)
