from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from aba_sdk import(
    PaywayConfig,
    PaywayClient,
    Environment,
    PaywayAPIError,
    PaywayRequestError,
)
from aba_sdk.models import QRRequest, Currency, PaymentOption, QRImageTemplate
from aba_sdk.utils import encode_items, encode_url
from aba_sdk.utils.timestamp import get_req_time

def main():
    config = PaywayConfig(
        merchant_id="eroxisabaypay",
        api_key="22e9e0cf-d5b4-4a31-82db-bc1046b20dac",
        env=Environment.sandbox,
    )
    client = PaywayClient(config)
    print(f"client:{client}")

    itmes = encode_items([
        {"name": "Coffee", "quantity": 1, "price": 3.5},
        {"name": "Bagel", "quantity": 2, "price": 2.0},
    ])

    tran_id = f"ORDER-{get_req_time()}"

    request = QRRequest(
        tran_id=tran_id,
        amount=1000,
        currency=Currency.KHR,
        payment_option=PaymentOption.ABAPAY_KHQR,
        first_name="Dara",
        last_name="Keng",
        email="dara@example.com",
        phone="012345678",
        items=itmes,
        # callback_url=encode_url("https://api.yoursite.com/payway/callback"),
        lifetime=6,
        qr_image_template=QRImageTemplate.TEMPLATE3_COLOR,
    )

    try:
        response = client.qr.generate_qr(request)
    except PaywayAPIError as e:
        print(f"API Error [{e.code}]: {e.message}")
        sys.exit(1)
    except PaywayRequestError as e:
        print(f"Network Error: {e}")
        sys.exit(1)

    print("\n QR Generated Successfully")
    print(f"   Status    : {response.status.message}")
    print(f"   Tran ID   : {response.tran_id or tran_id}")
    print(f"   Trace ID  : {response.status.trace_id}")
    print(f"   Amount    : {response.currency} {response.amount}")
    print(f"   QR String : {response.qr_string}")
    print(f"   Deeplink  : {response.abapay_deeplink[:60]}...")
 
    # Save QR image to disk
    output_path = "qr_code.png"
    response.save_qr_image(output_path)
    print(f"\nQR image saved to: {output_path}")
 
 
if __name__ == "__main__":
    main()
 