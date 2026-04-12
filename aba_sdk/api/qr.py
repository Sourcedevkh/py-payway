from ..api.base import BaseClient
from ..config import PaywayConfig
from ..models.qr import QRRequest, QRResponse
from ..exceptions import PaywayAPIError
from ..utils.hash import generate_hash
from ..utils.timestamp import get_req_time

_ENDPOINT = "api/payment-gateway/v1/payments/generate-qr"

class QRClient(BaseClient):
    def __init__(self, config: PaywayConfig) -> None:
        super().__init__(config)

    def generate_qr(self, request: QRRequest) -> QRResponse:

        request.req_time = get_req_time()
        request.merchant_id = self.config.merchant_id
        request.hash = generate_hash(
            self.config.api_key,
            *request.hash_values()
        )
        payload = request.to_payload()
        raw = self._post(_ENDPOINT, payload)

        #validate api status
        status = raw.get("status", {})
        if status.get("code") !="0":
            raise PaywayAPIError(
                code=status.get("code", "unknown"),
                message=status.get("message", "unknown error"),
                trace_id=status.get("trace_id", "unknown")
            )
        return QRResponse.from_dict(raw)