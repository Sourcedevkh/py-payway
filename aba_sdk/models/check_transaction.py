from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

# Request
@dataclass
class CheckTransactionRequest:
    tran_id: str

    # Filled auto by the client 
    req_time: str = ""
    merchant_id: str = ""
    hash: str = ""

    def to_payload(self) -> dict:
        return {
            "req_time": self.req_time,
            "merchant_id": self.merchant_id,
            "tran_id": self.tran_id,
            "hash": self.hash,
        }
    def hash_values(self) -> tuple:
        return (
            self.req_time,
            self.merchant_id,
            self.tran_id,
        )

# Response
@dataclass
class CheckTransactionStatus:
    code: str
    message: str
    tran_id: str

    @classmethod
    def from_dict(cls, data: dict) -> "CheckTransactionStatus":
        return cls(
            code=data.get("code", ""),
            message=data.get("message", ""),
            tran_id=data.get("tran_id", ""),
        )
    @property
    def is_success(self) -> bool:
        return self.code == "00"


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