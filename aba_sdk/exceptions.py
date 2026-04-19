class PaywayError(Exception):
    """Base exception for all Payway SDK errors."""
    pass

class PaywayAPIError(PaywayError):
    def __init__(self, code: str, message: str, trace_id: str = ""):
        self.code = code
        self.message = message
        self.trace_id = trace_id
        super().__init__(f"[{code}] {message} (trace_id={trace_id})")

class PaywayRequestError(PaywayError):
    """Raised when there is a network or request-level error."""
    pass


class PaywayValidationError(PaywayError):
    """Raised when request params fail validation."""
    pass


# Backward-compatible aliases.
PayWayError = PaywayError
PayWayAPIError = PaywayAPIError
PayWayRequestError = PaywayRequestError
PayWayValidationError = PaywayValidationError
