import base64
import json


def encode_base64(value: str) -> str:
    return base64.b64encode(value.encode("utf-8")).decode("utf-8")

def encode_items(items: list[dict]) -> str:
    return encode_base64(json.dumps(items, separators=(",", ":")))

def encode_url(url: str) -> str:
    return encode_base64(url)