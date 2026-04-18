from .config import PaywayConfig, Environment
from .api.qr import QRClient
from .api.transaction_client import CheckTransactionClient

class PaywayClient:
    def __init__(self, config: PaywayConfig) -> None:
        self.config = config
        self.qr = QRClient(config)
        self.check_transaction=CheckTransactionClient(config)

    def __repr__(self) -> str:
        env = self.config.env.value
        return f"PayWayClient(merchant_id={self.config.merchant_id!r}, env={env!r})"