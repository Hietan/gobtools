import json
from urllib.parse import urljoin

import requests


class Client:
    def __init__(self, path_root: str) -> None:
        self.path_root = path_root

    def is_connected(self) -> bool:
        request = requests.get(self.path_root, timeout=5)
        status_code = request.status_code

        success_min = 200
        client_error_max = 499
        return status_code >= success_min and status_code <= client_error_max

    def post_dict(self, path: str, data: dict) -> dict:
        request = requests.post(urljoin(self.path_root, path), json=data, timeout=None)  # noqa: S113
        return json.loads(request.text)
