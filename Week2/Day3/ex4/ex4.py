users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

dt1={}

for i,user in enumerate(users):
    dt1[user]=i
print(dt1)

dt2={}
for i,user in enumerate(users):
    dt2[i]=user
print(dt2)

users.sort()
dt3={}
for i,user in enumerate(users):
    dt3[user]=i
print(dt3)
