#ex1
my_fav_numbers ={77,24,1,97,19}
print(my_fav_numbers)
my_fav_numbers.add(34)
my_fav_numbers.add(78)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers ={1,2,3,4,5}
print(friend_fav_numbers)
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#ex2
#the aanswer is no tuple are immutable

#ex3
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.append("Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

#ex4
#a number with a decimal point,in range you can do it
my_list=[]
i=1.5
while(i<=5.5):
    my_list.append(i)
    i+=0.5

print(my_list)

#ex5
for i in range(1,21):
    print(i)
print("\n")
for i in range(1,21):
    if(i%2==0):
        print(i)

#ex6
my_name="david"
name=input("enter a name:").lower()
while(name!=my_name):
    name=input("enter a name:").lower()

#ex7
# Ask the user to input their favorite fruits
favorite_fruits_str = input("Enter your favorite fruit(s), separated by a space: ")
favorite_fruits = favorite_fruits_str.split()

# Ask the user to input a fruit
chosen_fruit = input("Enter a fruit: ")

# Check if the chosen fruit is in the favorite fruits list
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")

#ex8
cost=10
topping=input("enter a topping for your pizza for quiting adding a topping type quit:")
while(topping!="quit"):
    cost+=2.5
    print(f"you have added {topping} on your pizza")
    topping=input("enter a topping for your pizza for quiting adding a topping type quit:")

print(f"the tootal cost of your pizza is:{cost}")

#ex9
total_cost = 0

while True:
    age_str = input("Enter the age of a family member (or 'done' if finished): ")
    if age_str == 'done':
        break
    age = int(age_str)
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price

print("The total cost of all tickets is $", total_cost)
######################################################################
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]
allowed_names = []

for name in names:
    age_str = input("Enter the age of {}: ".format(name))
    age = int(age_str)
    if age >= 16 and age <= 21:
        allowed_names.append(name)

print("The following teenagers are allowed to watch the movie:", allowed_names)


#ex10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
for i in range(len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders.pop())
    print(f"the {finished_sandwiches[i]} is ready!")

#ex11
# define sandwich orders list
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]

# print message for running out of pastrami
print("Sorry, we have run out of pastrami sandwiches.")

# remove all occurrences of pastrami sandwiches using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# define finished sandwiches list
finished_sandwiches = []

# simulate making each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print("I'm making a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are ready!")
print("List of finished sandwiches: ", finished_sandwiches)
