#COLLECT A STRING

def find_string(a):
    b = list(a)
    c = len(b)
    val = b[0]+b[ c-1]
    return val
print(find_string("python"))
print(find_string("satya"))

#User Def functions
# Write function to concatenate three strings

def collect_string(str1, str2, str3):
     con = str1 + str2 + str3
     return con
print(collect_string("alpha", "beta", "gamma"))


#Write a function multiply three different integers and return a int

def integers(a, b, c):
    d = a * b * c
    return int(d)
print(integers(10,20,20))
print(integers(2.5,3.5,7))

#Write a function to check a string is palindrom or not

def palindrom(a):
    if a == a[::-1]:
        return "Palindrom"
    else :
        return "Not Palindrom"
print(palindrom("malayalam"))
print(palindrom("satya"))

# Write a function to return middle char of the string

def middle_char(a):
    b = len(a) // 2
    return a[b]
print(middle_char("python"))
print(middle_char("satya"))


#write a function to return whether middle character is vowel or not
def vowel(a):
    b = len(a) // 2
    c = a[b]
    if any((c=='a', c == 'e', c == 'i', c == 'o', c == 'u')):
        return "Vowel"
    else :
        return "Not Vowel"
    
print(vowel("satya"))
print(vowel("aeiou"))

#check whether number is prime or no

def prime(b):
    for i in range(2, b-1):
        if b % i != 0:
            return "prime number"
        else:
            return "Not a Prime number"
print(prime(17))
print(prime(20))

#check whether number is armstrong number or no

def arm(b):
    temp = int(b)
    sum = 0
    while temp!=0:
        k = temp%10
        sum += k*k*k
        temp = temp//10
    if sum == b:
        return "Given number is Armstrong number"
    else :
        return "Given number is not Armstrong number"
print(arm(153))
print(arm(180))

# Find factorial of a number
def factorial(fact):
    k = 1
    for i in range(1, fact+1):
        k = k*i
    return k
print(factorial(6))


#Find Fibnacci series
def fibnacci(ser):
    n1, n2 = 0, 1

    count = 0

    if ser <=0:
        return "please enter a positivie number"
    elif ser ==1 or ser == 2:
     return 1
    else :
        for i in range(1, ser):
            c = n1 + n2
            n1 = n2
            n2 = c
        return n2
print(fibnacci(9))
            

#Find factors of a number
def factor(a):
    for i in range(1, a+1):
        if a % i == 0:
            print(i)
            
print(factor(12))
print(factor(9))
print(factor(10))
























