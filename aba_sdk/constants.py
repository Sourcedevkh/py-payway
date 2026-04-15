from enum import Enum

class Environment(str, Enum):
    sandbox = "sandbox"
    production = "production"

BASE_URLS = {
    Environment.sandbox: "https://checkout-sandbox.payway.com.kh",
    Environment.production: "https://checkout.payway.com.kh"
}
