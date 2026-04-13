from dataclasses import dataclass

@dataclass
class BaseStatus:
    code: str
    message: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            code=data.get("code", ""),
            message=data.get("message", "")
        )

# QR status response
@dataclass
class QRStatus(BaseStatus):
    trace_id: str
    
    @classmethod
    def from_dict(cls, data: dict) -> "QRStatus":
        return cls(
            code=data.get("code", ""),
            message=data.get("message", ""),
            trace_id=data.get("trace_id", "")
        )
    @property
    def is_success(self) -> bool:
        
        # ABA use "0" for success
        return self.code == "0"


# check transaction status response
@dataclass
class CheckTransactionStatus(BaseStatus):
    tran_id: str

    @classmethod
    def from_dict(cls, data: dict) -> "CheckTransactionStatus":
        return cls(
            code=data.get("code", ""),
            message=data.get("message", ""),
            tran_id=data.get("tran_id", "")
        )
    @property
    def is_success(self) -> bool:

        # ABA use "00" for success
        return self.code == "00"
