import json


def json_format(obj: dict, indent: int = 4, sort_keys: bool = False) -> str:
    return json.dumps(obj, indent=indent, sort_keys=sort_keys)
