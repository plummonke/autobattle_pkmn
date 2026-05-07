from exception import Exception

class ServiceInitializationError(Exception):
    def __init__(self, reason: str):
        self.message = f'PokeAPI Service initialization failed due to {reason}.'

    def __str__(self):
        return self.message
