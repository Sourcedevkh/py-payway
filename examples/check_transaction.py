from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from aba_sdk import (
    PayWayClient,
    PaywayConfig,
    Environment,
    PayWayAPIError,
    PayWayRequestError
)

def main():
    config = PaywayConfig(
        merchant_id="eroxisabaypay",
        api_key="22e9e0cf-d5b4-4a31-82db-bc1046b20dac",
        env=Environment.sandbox
    )

    client=PayWayClient(config)

    tran_id = "ORDER-20260413143035"

    try:
        response = client.check_transaction.check(tran_id)
    except PayWayAPIError as e:
        print(f"API Error [{e.code}]: {e.message}")
        sys.exit(1)
    except PayWayRequestError as e:
        print(f"Network Error: {e}")
        sys.exit(1)

    data = response.data
    print("\nTransaction checked")
    print(f" tran_id: {response.status.tran_id}")
    print(f" Payment status: {data.payment_status}")
    print(f"   Amount Paid     : {data.payment_currency} {data.payment_amount}")
    print(f"   Original Amount : {data.original_amount}")
    print(f"   Payment Currency: {data.payment_currency}")
    print(f"   Refund Amount   : {data.refund_amount}")
    print(f"   APV             : {data.apv}")
    print(f"   Date            : {data.transaction_date}")

    if data.is_approved:
        print("\n🟢 Payment APPROVED — safe to fulfil the order")
    elif data.is_pending:
        print("\n🟡 Payment PENDING — customer hasn't paid yet")
    else:
        print(f"\n🔴 Payment status: {data.payment_status}")
 
 
if __name__ == "__main__":
    main()