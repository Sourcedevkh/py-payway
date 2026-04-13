from .base import BaseClient
from ..models.qr import QRRequest, QRResponse

class QRClient(BaseClient):

    _ENDPOINT = "api/payment-gateway/v1/payments/generate-qr"

    def generate_qr(self, request: QRRequest) -> QRResponse:
        return self._prepare_and_validate(
            endpoint=self._ENDPOINT,
            request=request,
            response_class=QRResponse,
            success_code="0"
        )