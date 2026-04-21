import base64
import os

def save_base64_image(b64_string: str, filepath: str) -> str:
    ''' Decodes a base64 string and save it to the specified path
        Supported both raw base64 and data urls formats'''
    
    # handle the data:image/png;base64
    if "," in b64_string:
        _, b64_string = b64_string.split(",", 1)

    image_bytes = base64.b64decode(b64_string)

    # ensure the directory exists
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)

    with open(filepath, "wb") as f:
        f.write(image_bytes)
    return filepath