from dataclasses import dataclass

@dataclass
class QRStatus:
    code: str
    message: str
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
  