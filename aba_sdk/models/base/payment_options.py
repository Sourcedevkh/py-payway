from enum import Enum

class PaymentOption(str, Enum):

    ABAPAY = "abapay"
    KHQR = "khqr"
    ABAPAY_KHQR = "abapay_khqr"
    WECHAT = "wechat"
    ALIPAY = "alipay"

    ## Note: Alipay & WeChat do not support pre-auth