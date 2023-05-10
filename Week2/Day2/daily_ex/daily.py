#ex1
num=int(input("enter a number:"))
length=int(input("enter the length:"))
list=[]
for i in range(1,(length+1)):
    list.append(num*i)

print(list)

#ex2
user_input = input("Enter a string: ")
output = user_input[0]

for i in range(1, len(user_input)):
    if user_input[i] != user_input[i-1]:
        output += user_input[i]

print("String with consecutive duplicates removed:", output)
