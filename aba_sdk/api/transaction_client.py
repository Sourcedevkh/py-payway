from .base import BaseClient
from ..models.check_transaction import CheckTransactionRequest, CheckTransactionResponse
from ..models.close_transaction import CloseTransactionRequest, CloseTransactionResponse

class TransactionClient(BaseClient):

    _ENDPOINT_CHECK = "api/payment-gateway/v1/payments/check-transaction-2"
    _ENDPOINT_CLOSE = "api/payment-gateway/v1/payments/close-transaction"

    def check(self, tran_id: str) -> CheckTransactionResponse:
        request = CheckTransactionRequest(tran_id=tran_id)
        return self._prepare_and_validate(self._ENDPOINT_CHECK, request, CheckTransactionResponse)

    def close(self, tran_id: str) -> CloseTransactionResponse:
        request = CloseTransactionRequest(tran_id=tran_id)
        return self._prepare_and_validate(self._ENDPOINT_CLOSE, request, CloseTransactionResponse)


CheckTransactionClient = TransactionClient

__all__ = ["TransactionClient", "CheckTransactionClient"]