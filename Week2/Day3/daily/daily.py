#ex1
word = input("Enter a word: ")
letter_indexes = {}

for index, letter in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter] = [index]

print(letter_indexes)


#ex2
wallet=float(input("enter sum of money: "))

items_purchase1= {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

affordable_items = []
for item, price in items_purchase1.items():
    item_price = float(price.replace('$', '').replace(',', ''))
    if item_price <= wallet:
        affordable_items.append(item)


affordable_items.sort()
if affordable_items:
    print("You can afford the following items:")
    for item in affordable_items:
        print("- " + item)
else:
    print("Nothing")
