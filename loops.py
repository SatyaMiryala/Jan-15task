#Task1:
'''
#Using Range function  print multiples of 5 from 0 to 75

for i in range(0,76):
    if i%5 == 0:
        print(i)

#Using Range function  print multiples of 8 from 0 to 72
for var in range(0,73):
    if var%8 == 0:
        print(var)

#Using Range function  print multiples of 5 from 75 to 0
for a in range(75,0,-1):
    if a%5 == 0:
        print(a)
        
#Using Range function  print multiples of 8 from 96 to 72
for var1 in range(96, 72, -1):
    if var1%8 == 0:
        print(var1)

'''
#Task2:

#Get a dynamic list from user

a = int(input("please enter a number"))
b = int(input("please enter a number"))

for i in range(a, b):
    print(i)
    print(type(i))
