import json
import ssl
import urllib.request
import urllib.error

from ..config import PaywayConfig
from ..exceptions import PaywayAPIError, PaywayRequestError


class BaseClient:
    """
    Thin HTTP client that wraps urllib for zero extra dependencies.
    Override with httpx/requests if preferred.
    """

    def __init__(self, config: PaywayConfig) -> None:
        self.config = config

    def _build_url(self, path: str) -> str:
        return f"{self.config.base_url}/{path.lstrip('/')}"

    def _ssl_context(self) -> ssl.SSLContext:
        """Build a verified SSL context, preferring certifi when installed."""
        try:
            import certifi  # type: ignore

            return ssl.create_default_context(cafile=certifi.where())
        except Exception:
            return ssl.create_default_context()

    def _post(self, path: str, payload: dict) -> dict:
        """
        Send a POST request with a JSON body and return the parsed response.

        Raises:
            PaywayRequestError: On network / timeout errors.
            PaywayAPIError: When the API returns a non-success status code.
        """
        url = self._build_url(path)
        body = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            url=url,
            data=body,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (compatible; aba-payway-sdk/0.1)",
            },
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=self.config.timeout,
                context=self._ssl_context(),
            ) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw)

        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8")
            try:
                data = json.loads(raw)
                status = data.get("status", {})
                raise PaywayAPIError(
                    code=status.get("code", str(exc.code)),
                    message=status.get("message", exc.reason),
                    trace_id=status.get("trace_id", ""),
                ) from exc
            except (json.JSONDecodeError, KeyError):
                raise PaywayRequestError(
                    f"HTTP {exc.code}: {exc.reason} — {raw}"
                ) from exc

        except urllib.error.URLError as exc:
            raise PaywayRequestError(
                f"Network error contacting PayWay: {exc.reason}"
            ) from exc

        except TimeoutError as exc:
            raise PaywayRequestError(
                f"Request timed out after {self.config.timeout}s"
            ) from exc
