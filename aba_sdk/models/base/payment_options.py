from enum import Enum

class PaymentOption(str, Enum):

    ''' Supported payment options:
        - abapay_khqr : Payway will response ABA KHQR.
        - wechat : PayWay will respond with a WeChat QR (only for USD transactions)
        - alipay : PayWay will respond with an Alipay QR (only for USD transactions) '''

    ABAPAY = "abapay"
    KHQR = "khqr"
    ABAPAY_KHQR = "abapay_khqr"
    WECHAT = "wechat"
    ALIPAY = "alipay"

    ## Note: Alipay & WeChat do not support pre-auth