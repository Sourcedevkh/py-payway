from ..api.base import BaseClient
from ..config import PaywayConfig
from ..exceptions import PaywayAPIError
from ..models.check_transaction import CheckTransactionRequest, CheckTransactionResponse
from ..utils.hash import generate_hash
from ..utils.timestamp import get_req_time

_ENDPOINT = "api/payment-gateway/v1/payments/check-transaction-2"

class CheckTransactionClient(BaseClient):
    def __init__(self, config: PaywayConfig) -> None:
        super().__init__(config)
    def check(self, tran_id: str) -> CheckTransactionResponse:
        request = CheckTransactionRequest(tran_id=tran_id)
        request.req_time = get_req_time()
        request.merchant_id = self.config.merchant_id

        request.hash = generate_hash(self.config.api_key, *request.hash_values())
        payload = request.to_payload()
        raw = self._post(_ENDPOINT, payload)

        #validate api status
        status = raw.get("status", {})
        if status.get("code") != "00":
            raise PaywayAPIError(
                code=status.get("code", "unknown"),
                message=status.get("message", "unknown error"),
                trace_id=status.get("trace_id", "")
            )
        return CheckTransactionResponse.from_dict(raw)