from dataclasses import dataclass
from .constants import BASE_URLS, Environment


@dataclass
class PaywayConfig:
    merchant_id: str
    api_key: str
    env: Environment = Environment.sandbox
    timeout: int = 30

    @property
    def base_url(self) -> str:
        if self.env == Environment.production:
            return BASE_URLS[self.env]
        return BASE_URLS[Environment.sandbox]
    @property
    def is_sandbox(self) -> bool:
        return self.env == Environment.sandbox