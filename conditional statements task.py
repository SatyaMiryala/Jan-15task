#len of the string odd or even

'''

str = len(input("please enter a string"))

if str%2 == 0:
    print("String is even")
else:
    print("string is odd")

    #mark calculation

#collect physics / checmistry / mathematics mark from user
#all the marks should be between 0 -200 ==> 
#calculate aggregate = phy/4  + chem/4  + maths / 2

#pass mark: 70



#aggregate > 190 :  First class
    
#aggregate > 150 : second class
    
#aggregate > 70 : Third class 
    
#aggregate < 70 : Fail Try again
    
    
#valid or invalid
#Pass or Fail
#Class 


Physics  = int(input("Please enter Physics marks"))
chemistry  = int(input("Please enter chemistry marks"))
maths  = int(input("Please enter mathematics marks"))

Aggregate = Physics/4 + chemistry/4 + maths/2

print(Aggregate)

if Aggregate > 70 :
    print("Pass")
else :
    print("Fail")


if Aggregate > 190 :
    print("First class")
elif Aggregate > 150 :
    print("Second class")
elif Aggregate > 70 :
    print("Thrid class")
else :
    print("Fail try again")

    
#Fizz buzz
#Get one number from user
#5
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

a = int(input("Please enter a number"))


if (a % 3 == 0 and a % 5 ==0 ):
    print("Fizzbuzz")

elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0 :
    print("Fizz")
else :
    print("None")

'''

#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL


#93 ===> A
#99 ===> A
#88 ====> B

#78

#VALID MARK (between 0 to 100)
#PASS MARK ()
#C

b = int(input("Please enter your marks"))

if (b <= 0 or b >= 100) :
    print("invalid number")
else :
    print("valid Marks")
    if (b > 90 and b <100) :
        print("A")
    elif (b > 80 and b <89) :
        print("B")
    elif (b > 70 and b <79):
        print("C")
    elif (b > 60 and b <69):
        print("D")
    elif print(b > 50 and b <59):
        print("E")
    else :
        print("Fail")




