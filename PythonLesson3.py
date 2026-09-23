from functools import reduce


def calculate_price(*prices):
    lst = []
    for i in prices:
        lst.append(i*100)
    return lst

def show_order(customer,product,quantity):
    print("Order details\n",customer," ",product," ",quantity)

print(calculate_price())
print(calculate_price(23))
print(calculate_price(45,65,76))

order = {
    "customer": "Ajay",
    "product": "Laptop",
    "quantity": 2
}
show_order(**order)


products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 12000}
]

products.sort(key=lambda x: x['price'])
print(products)

prices = [100, 200, 300]
res =map(lambda x : x>100 , prices)
res_reduce = reduce(lambda total, price : total+price,prices)
print(list(res))
print(res_reduce)