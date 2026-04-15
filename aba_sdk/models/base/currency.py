from enum import Enum
class Currency(str, Enum):
    ''' Supported transaction currencies form ABA: KHR, USD '''
    KHR = "KHR"
    USD = "USD"