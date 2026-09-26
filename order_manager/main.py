from order_manager.exceptions import InvalidQuantityError, InvalidPriceError
from order_manager.models import create_order, calculate_total
from order_manager.storage import load_orders, save_orders, export_csv


def main():
    try:
        orders = load_orders()

        new_order = create_order(
            order_id=101,
            customer="Ajay",
            product="Laptop",
            quantity=2,
            price=60000
        )

        orders.append(new_order)
        save_orders(orders)
        export_csv(orders)
        total = calculate_total(new_order)

        print("Order created successfully!")
        print("----------------------------")
        print(f"Order ID: {new_order['order_id']}")
        print(f"Customer: {new_order['customer']}")
        print(f"Product: {new_order['product']}")
        print(f"Quantity: {new_order['quantity']}")
        print(f"Price: ₹{new_order['price']}")
        print(f"Total: ₹{total}")

    except InvalidQuantityError as error:
        print("Order failed ",error)
    except InvalidPriceError as error:
        print("Order failed",error)

if __name__ == "__main__":
    main()