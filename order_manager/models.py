from order_manager.exceptions import InvalidQuantityError, InvalidPriceError


def create_order(order_id,customer,product,quantity,price):
    if quantity <=0:
        raise InvalidQuantityError("Quantity should be greater than zero")
    if price <=0:
        raise InvalidPriceError("Price should be greater than zero")
    return {
        "order_id":order_id,
        "customer":customer,
        "product":product,
        "quantity":quantity,
        "price":price
    }

def calculate_total(order):
    return order["quantity"] * order["price"]