from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .base.qr_status import QRStatus
from .base.qrImage_template import QRImageTemplate
from .base.purchase_types import PurchaseType
from .base.payment_options import PaymentOption
from .base.currency import Currency
from ..utils.save_images import save_base64_image


# Request
@dataclass
class QRRequest:

    # Required fields
    tran_id: str
    amount: float
    currency: Currency
    payment_option: PaymentOption

    # customer info (required by api)
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    phone: str = ""

    # Optional fields
    purchase_type: PurchaseType = PurchaseType.PURCHASE
    items: Optional[str] = None          # Base64-encoded JSON
    callback_url: Optional[str] = None   # Base64-encoded URL
    return_deeplink: Optional[str] = None
    custom_fields: Optional[str] = None
    return_params: Optional[str] = None
    payout: Optional[str] = None
    lifetime: int = 6                   # QR lifetime in minutes
    qr_image_template: QRImageTemplate = QRImageTemplate.TEMPLATE3_COLOR
 

    # filled auto by the client 
    req_time: str = ""
    merchant_id: str = ""
    hash: str = ""


    def to_payload(self) -> dict:
        payload = {
            "req_time": self.req_time,
            "merchant_id": self.merchant_id,
            "tran_id": self.tran_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "amount": self.amount,
            "purchase_type": self.purchase_type.value,
            "payment_option": self.payment_option.value,
            "items": self.items,
            "currency": self.currency.value,
            "callback_url": self.callback_url,
            "custom_fields": self.custom_fields,
            "return_params": self.return_params,
            "payout": self.payout,
            "lifetime": self.lifetime,
            "qr_image_template": self.qr_image_template.value,
            "hash": self.hash,
        }
        # Remove None values
        return {
            k: v for k, v in payload.items()
            if v is not None
        }
    
    def hash_values(self) -> tuple:
        values = [
            self.req_time,
            self.merchant_id,
            self.tran_id,
            str(self.amount),
        ]

        if self.items is not None:
            values.append(self.items)

        values.extend([
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.purchase_type.value,
            self.payment_option.value,
        ])

        if self.callback_url is not None:
            values.append(self.callback_url)
        if self.return_deeplink is not None:
            values.append(self.return_deeplink)

        values.append(self.currency.value)

        if self.custom_fields is not None:
            values.append(self.custom_fields)
        if self.return_params is not None:
            values.append(self.return_params)
        if self.payout is not None:
            values.append(self.payout)
        values.append(str(self.lifetime))
        values.append(self.qr_image_template.value)
        return tuple(values)
 

# Response   
@dataclass
class QRResponse:
    tran_id: str
    qr_string: str
    qr_image: str
    abapay_deeplink: str
    app_store: str
    play_store: str
    amount: float
    currency: str
    status: QRStatus

    @classmethod
    def from_dict(cls, data: dict) -> "QRResponse":
        return cls(
            tran_id=data.get("tran_id") or data.get("tranId", ""),
            qr_string=data.get("qr_string") or data.get("qrString", ""),
            qr_image=data.get("qr_image") or data.get("qrImage", ""),
            abapay_deeplink=data.get("abapay_deeplink", ""),
            app_store=data.get("app_store", ""),
            play_store=data.get("play_store", ""),
            amount=data.get("amount", 0),
            currency=data.get("currency", ""),
            status=QRStatus.from_dict(data.get("status", {}))
        )

    ## Save the QRCode image
    def save_qr_image(self, filepath: str) -> None:
        save_base64_image(self.qr_image, filepath)


# Backward-compatible alias for common typo in examples.
PaymentOptions = PaymentOption

