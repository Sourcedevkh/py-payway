from dataclasses import dataclass

@dataclass
class DataRequest:
    ''' Shared base for all request structure for Check, Close transaction apis'''
    tran_id: str

    #filled auto by the client
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
        return(
            self.req_time,
            self.merchant_id,
            self.tran_id,
        )

# Create alias
CheckTransactionRequest = DataRequest
CloseTransactionRequest = DataRequest
