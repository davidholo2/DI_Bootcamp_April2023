sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
for i in range(len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders.pop())
    print(f"the {finished_sandwiches[i]} is ready!")