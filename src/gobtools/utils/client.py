import json
from urllib.parse import urljoin

import requests


class Client:
    def __init__(self, path_root: str) -> None:
        self.path_root = path_root

    def is_connected(self) -> bool:
        request = requests.get(self.path_root)
        status_code = request.status_code
        return status_code >= 200 and status_code < 500

    def post_dict(self, path: str, data: dict) -> dict:
        request = requests.post(urljoin(self.path_root, path), json=data)
        return json.loads(request.text)
