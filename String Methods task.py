#Task1:

#Get one string from user
#identify the middle character of the string
'''
input_collection =input("Please enter a string")

middle_index = len(input_collection) // 2

print(input_collection[middle_index])


#Task2:

#output: python  (strip,rstrip,lstrip method *)

string1 = "***python***"
string2 = "**python********"
string3 = "********java*******"

a = string1.strip("*")
b = string2.strip("*")
c = string3.strip("*")
d = string1.rstrip("*")
e = string2.rstrip("*")
f = string3.rstrip("*")
g = string1.lstrip("*")
h = string2.lstrip("*")
i = string3.lstrip("*")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)


#Task3: (name<space>float)

#collect three strings from user  name<space>float

#split + indexing

#10.30 + 12.19 + 20.20 ===> output ===> round (42.69000) 5 decimal places should be (format)

string1 = "ravi 10.30"  
string2 = "meghala 12.19"
string3 = "Gokul 20.20"

a =string1.split()
val1 = float(a[1])

b = string2.split()
val2 = float(b[1])

c = string3.split()
val3 = float(c[1])

d = val1+val2+val3

print(d)

#Task4:

#collect two strings from user

string1 = "python"
string2 = "java"

a = string1.replace("p","j")
b = string2.replace("j", "p")
c = string1[len(string1) // 2]
d = string2[len(string2) // 2]


val = a + b + str(64) + c + d
print(val)
#output ===> jythonpava64hv

string3 = "maths"
string4 = "science"

val1 = string3.replace("m","s")
val2 = string4.replace("s", "m")
val3 = string3[len(string3) // 2]
val4 = string4[len(string4) // 2]


e = val1 + val2 + str(57) + val3 + val4
print(e)

#output ===> sathsmcience57te


#Task5:

#Collect two strings from user

#output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
#(ord , chr)

string1 = "wikipedia"
string2 = "typescript"

a = string1[len(string1) // 2]

b = string2[len(string2) // 2]

print(a)
print(b)

print(ord(a) + ord(b))


#Task 7 Completed 
#string = "abracadabra"

string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print (string)
print(l)

'''

a = input("please enter")
b = a.swapcase()
print(b)











