items = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

for item, price in items.items():
    print(f"{item}: ${price}")

items = {
"banana": {"price": 4, "stock": 10},
"apple": {"price": 2, "stock": 5},
"orange": {"price": 1.5, "stock": 24},
"pear": {"price": 3, "stock": 1}
}

total_cost = 0

for item, info in items.items():
    item_cost = info["price"] * info["stock"]
    total_cost += item_cost

print(f"The total cost of all items in stock is ${total_cost:.2f}")