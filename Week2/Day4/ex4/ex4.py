import random

def is_equal(num):
    num1=random.randint(1,100)
    if(num1==num):
        print("success")
    else:
        print(f"fail num={num} random number={num1}")
num=50
if(num>0 and num<101):
    is_equal(num)

