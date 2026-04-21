from __future__ import annotations
from dataclasses import dataclass

from .base.qr_status import CloseTransactionStatus

# Response
@dataclass
class CloseTransactionResponse:
    status: CloseTransactionStatus

    @classmethod
    def from_dict(cls, raw: dict) -> "CloseTransactionResponse":
        return cls(
            status=CloseTransactionStatus.from_dict(raw.get("status", {})),
        )
    @property
    def is_cancelled(self) -> bool:

        # ABA use "00" for success
        return self.status.is_success
