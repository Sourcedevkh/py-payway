from datetime import datetime, timezone

def get_req_time() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y%m%d%H%M%S")
