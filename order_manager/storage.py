import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent/"data"
JSON_FILE = DATA_DIR/"order.json"
CSV_FILE = DATA_DIR/"orders.csv"

def load_orders():
    DATA_DIR.mkdir(exist_ok=True)
    if not JSON_FILE.exists():
        return []
    with JSON_FILE.open('r',encoding="utf-8") as file:
        return json.load(file)
def save_orders(orders):
    DATA_DIR.mkdir(exist_ok=True)
    with JSON_FILE.open("w",encoding="utf-8") as file:
        json.dump(
            orders,
            file,
            indent=4,
            ensure_ascii=False
        )
def export_csv(orders):
    DATA_DIR.mkdir(exist_ok=True)
    fieldname = [
        "order_id",
        "customer",
        "product",
        "quantity",
        "price"
    ]
    with CSV_FILE.open("w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(orders)