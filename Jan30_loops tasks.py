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


#Task2:

#Get a dynamic list from user

li1 = []
a = int(input("please enter a number"))
b = int(input("please enter a number"))

for i in range(a, b):
    li1.append(i)

print(li1)


#Task3:

#Get a dynamic dictionary from user

#clues Task2 and Task3
#1. get number of elements from user
#Loop through range
#append to list/dicti

di1 = []
di2 = []

a = int(input("Please enter a number"))
b = int(input("Please enter a number"))
c = int(input("Please enter a number"))
d = int(input("Please enter a number"))
for i in range(a, b):
    di1.append(i)
for g in range(c, d):
    di2.append(g)
val = zip(di2, di1)
print(dict(val))

#Task4:

#Get two integers from user
#print multiples of 8 between them

#clues:
#Use range function in for loop
#Use if condition inside for loop
#add in to list

#input 10 100
#multiples of 8

li1 = []

a = int(input("Please enter the element"))
b = int(input("Please enter the element"))

for i in range(a, b):
    if i % 8 == 0:
        li1.append(i)
print(li1)
    

#[16,24,32.....,96]


#Task5:


#Input:
li1 = [3,4,5,2,7,8,9,10]

even = []
odd = []

for i in li1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#check whether number is prime or no

b = int(input("please enter the element"))

for i in range(2, b-1):
    if b % i == 0:
        print("Composite number")
        break
else:
    print("prime_number")

#check whether number is armstrong number or no

arm = int(input("Please enter number"))

temp = arm
sum = 0
while temp!=0:
    k = temp%10
    print(k)
    sum += k*k*k
    print(sum)
    temp = temp//10
if sum == arm:
    print("Given number is Armstrong number")
else :
    print("Given number is not Armstrong number")

# Find factorial of a number

fact =int(input("please enter a number"))

k = 1
for i in range(1, fact+1):
    k = k*i
print("The factorial of given number is :",k)


#Find Fibnacci series

ser = int(input("please enter no of terms"))

n1, n2 = 0, 1

count = 0

if ser <=0:
    print("please enter a positivie number")
elif ser ==1:
    print("The fibnacci series is",ser,":")
    print(n1)
else :
    print("the fibonacci sequence:")
    while count < ser:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

'''
#Find factors of a number

a = int(input("please enter a number"))

for i in range(1, a+1):
    if a % i == 0:
         print(i)







    























