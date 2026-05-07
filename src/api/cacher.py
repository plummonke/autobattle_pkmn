import json

from datetime import date
from typing import Dict

class Cacher:
    def __init__(self, base_filename: str):
        today = date.today().strfmt('%Y%m%d')
        self.filename = 'cache/' + base_filename + today + '.json'

        self.create_new_file(filename)

    def create_new_file(self, filename: str):
        with open(filename, 'x') as f:
            f.write('{}')

    def write_to_file(self, data: Dict):
        with open(self.filename, 'wr') as f:
            file = json.load(f)
            file.update(Dict)
            json.dump(file, f)
