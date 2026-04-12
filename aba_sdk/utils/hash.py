import hashlib
import hmac
import base64

def generate_hash(api_key: str, *values: str) -> str:
    """
    Generate HMAC-SHA512 hash for request signing
 
    Args:
        api_key: The merchant's API key (used as the HMAC secret).
        *values: Ordered parameter values to include in the hash.
                 Pass only the values that are present in your request.
 
    Returns:
        Base64-encoded HMAC-SHA512 digest string.
 
    Example:
        hash_str = generate_hash(api_key, req_time, merchant_id, tran_id, amount, ...)
    """

    message = "".join(str(v) for v in values)
    digest = hmac.new(
        key=api_key.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha512,
    ).digest()
    return base64.b64encode(digest).decode("utf-8")
 
 