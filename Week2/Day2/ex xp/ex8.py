cost=10
topping=input("enter a topping for your pizza for quiting adding a topping type quit:")
while(topping!="quit"):
    cost+=2.5
    print(f"you have added {topping} on your pizza")
    topping=input("enter a topping for your pizza for quiting adding a topping type quit:")

print(f"the tootal cost of your pizza is:{cost}")