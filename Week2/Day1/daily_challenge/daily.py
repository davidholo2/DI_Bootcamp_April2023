import random

str1 = input("enter a string that is 10 characters long:")
if (len(str1) > 10):
    print("i said 10 characters long not more then 10!")
elif (len(str1) < 10):
    print("i said 10 characters long not less then 10!")
else:
    str_add = ""
    for i in range(10):
        str_add += str1[i]
        print(str_add)

string_list = list(str1)
random.shuffle(string_list)
jumbled_string = ''.join(string_list)
print("Jumbled string:", jumbled_string)
