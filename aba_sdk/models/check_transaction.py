from __future__ import annotations
from dataclasses import dataclass

from .base.qr_status import CheckTransactionStatus

# Responese data
@dataclass
class CheckTransactionData:
    payment_status_code: int
    total_amount: float
    original_amount: float
    refund_amount: float
    discount_amount: float
    payment_amount: float
    payment_currency: str
    apv: str
    payment_status: str
    transaction_date: str


    @classmethod
    def from_dict(cls, data: dict) -> "CheckTransactionData":
        return cls(
            payment_status_code= int(data.get("payment_status_code", -1)),
            total_amount=float(data.get("total_amount", 0)),
            original_amount=float(data.get("original_amount", 0)),
            refund_amount=float(data.get("refund_amount", 0)),
            discount_amount=float(data.get("discount_amount", 0)),
            payment_amount=float(data.get("payment_amount",0)),
            payment_currency=data.get("payment_currency", ""),
            apv=data.get("apv", ""),
            payment_status=data.get("payment_status", ""),
            transaction_date=data.get("transaction_date", ""),
        )
    @property
    def is_approved(self) -> bool:
        return self.payment_status == "APPROVED"
    @property
    def is_pending(self) -> bool:
        return self.payment_status == "PENDING"

@dataclass
class CheckTransactionResponse:
    data: CheckTransactionData
    status: CheckTransactionStatus

    @classmethod
    def from_dict(cls, raw: dict) -> "CheckTransactionResponse":
        return cls(
            data=CheckTransactionData.from_dict(raw.get("data", {})),
            status=CheckTransactionStatus.from_dict(raw.get("status", {}))
        )