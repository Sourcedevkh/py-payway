from .config import PaywayConfig, Environment
from .api.qr import QRClient
from .api.transaction_client import TransactionClient

class PaywayClient:
    def __init__(self, config: PaywayConfig) -> None:
        self.config = config
        self.qr = QRClient(config)
        transaction_client = TransactionClient(config)
        self.check_transaction = transaction_client
        self.close_transaction = transaction_client

    def __repr__(self) -> str:
        env = self.config.env.value
        return f"PayWayClient(merchant_id={self.config.merchant_id!r}, env={env!r})"