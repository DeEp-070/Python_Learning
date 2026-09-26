class OrderError(Exception):
    pass
class InvalidQuantityError(OrderError):
    pass
class InvalidPriceError(OrderError):
    pass