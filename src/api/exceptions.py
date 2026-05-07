from exception import Exception

class ServiceInitializationError(Exception):
    def __init__(self, reason: str):
        self.message = f'PokeAPI Service initialization failed due to {reason}.'

    def __str__(self):
        return self.message

class EndpointRequestError(Exception):
    def __init__(self, endpoint_name: str, code: int):
        self.message = f'{endpoint_name} failed with HTTP status code {code}.'

    def __str__(self):
        return self.message
