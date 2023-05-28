#ex1
for i in range(4):
    print("hello world")

#ex2
result=(99**3)*8
print(result)

#ex3
>>> 5 < 3
#false
>>> 3 == 3
#true
>>> 3 == "3"
#false
>>>"3" > 3
#False
>>> "Hello" == "hello"
#false

#ex4
computer_brand ="asus"
print("I have a "+computer_brand+" computer")

#ex5
name="David"
age=21
shoe_size=44
info="my name is "+name+" my age is "+str(age)+ " and my shoe size is "+str(shoe_size)
print(info)

#ex6
import time

a=int(input("enter a num: "))
b=int(input("enter a num: "))
if(a>b):
    print("hello world")
    time.sleep(5)

#ex7
import time

a=int(input("enter a num: "))
if(a%2==0):
    print("even")
    time.sleep(5)
else:
    print("odd")
    time.sleep(5)

#ex8
import time
my_name = "david"
user_name = input("enter your name: ").lower()
if (my_name == user_name):
    print("even wow we are the same!")
    time.sleep(5)
else:
    print("i knew you dont have a cool name like mine")
    time.sleep(5)

#ex9
# 57.0866 iches=145 cm
import time

height = int(input("enter your height : "))
if (height >= 57.0866):
    print("you can enter")
    time.sleep(5)
else:
    print("you are small for this ride try agian next year when you grow a little")
    time.sleep(5)
