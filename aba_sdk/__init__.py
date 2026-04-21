"""
ABA PayWay Python SDK

Quick start::

    from aba_payway import PayWayClient, PayWayConfig, Environment
    from aba_payway.models import QRRequest, Currency, PaymentOption

    config = PayWayConfig(
        merchant_id="your_merchant_id",
        api_key="your_api_key",
        environment=Environment.SANDBOX,
    )
    client = PayWayClient(config)
"""

from .client import PaywayClient
from .config import PaywayConfig, Environment

from .exceptions import (
    PaywayError,
    PaywayAPIError,
    PaywayRequestError,
    PaywayValidationError,
)
from .models import (
    # QR
    Currency,
    PaymentOption,
    PaymentOptions,
    PurchaseType,
    QRImageTemplate,
    QRRequest,
    QRResponse,
    QRStatus,

    #check transaction
    CheckTransactionRequest,
    CheckTransactionResponse,
    CheckTransactionData,
    CheckTransactionStatus,

    #close transaction
    CloseTransactionRequest,
    CloseTransactionResponse,
    CloseTransactionStatus,
)

# Backward-compatible aliases.
PayWayClient = PaywayClient
PayWayConfig = PaywayConfig
PayWayError = PaywayError
PayWayAPIError = PaywayAPIError
PayWayRequestError = PaywayRequestError
PayWayValidationError = PaywayValidationError

__all__ = [
    # Client
    "PaywayClient",
    "PaywayConfig",
    "PayWayClient",
    "PayWayConfig",
    "Environment",
    # Exceptions
    "PaywayError",
    "PaywayAPIError",
    "PaywayRequestError",
    "PaywayValidationError",
    "PayWayError",
    "PayWayAPIError",
    "PayWayRequestError",
    "PayWayValidationError",
    # Models
    "Currency",
    "PaymentOption",
    "PaymentOptions",
    "PurchaseType",
    "QRImageTemplate",
    "QRRequest",
    "QRResponse",
    "QRStatus",

    #check transaction
    "CheckTransactionRequest",
    "CheckTransactionResponse",
    "CheckTransactionData",
    "CheckTransactionStatus",

    #close transaction
    "CloseTransactionRequest",
    "CloseTransactionResponse",
    "CloseTransactionStatus",
]

__version__ = "0.1.2"
