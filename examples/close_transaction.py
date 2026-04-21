from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from aba_sdk import(
    PayWayClient,
    PaywayConfig,
    Environment,
    PayWayAPIError,
    PayWayRequestError
)

def main():
    config = PaywayConfig(
        merchant_id="your_merchant_id",
        api_key="your_api_key",
        env=Environment.sandbox
    )
    client = PayWayClient(config)

    tran_id = "ORDER-20260413143035"

    try:
        response = client.close_transaction.close(tran_id)
    except PayWayAPIError as e:
        print(f"API error [{e.code}]: {e.message}")
        sys.exit(1)
    except PayWayRequestError as e:
        print(f"Network error: {e}")
        sys.exit(1)
    
    if response.is_cancelled:
        print(f"\nTransaction '{response.status.tran_id}' has been cancelled")
        print(" - Payment will be rejected or reversed.")
        print(" - No callback will be sent to the merchant.")
    else:
        print(f"\nFailed to cancel: [{response.status.code}] {response.status.message}")

if __name__ == "__main__":
    main()
 