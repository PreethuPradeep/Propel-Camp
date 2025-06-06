#Conditional Statement

 

age=int(input("enter your age"))
if age>18:
    print("YOU ARE AN ADULT")

#check wheather a number is positive
num=int(input("eneter a number"))
if num>0:
    print("POSITIVE")

#If-else statement

age=int(input("Enter your age"))
if age>18:
    print("YOU ARE AN ADULT")
else:
    print("You are a kid")

#write a program to check if the number is odd or even

num=int(input("enter a number"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

# #ask the user to enter a number and print whether it is positive or negative
a=int(input("enter a number"))
if a>=0:
    print("positive")
else:
    print("negative")
# Take two numbers from the user and print which is greater
a=int(input("enter a number"))
b=int(input("input a number"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
# Ask the user their age. If they are 18 or older then you are eligible to vote
# if not you are not eligible to vote 
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible to vote")

#Elif Statement 

score=int(input("Enter your score"))
if score>=90:
    print("Grade A")
elif score>=75:
    print("Grade B")
elif score>=50:
    print("Grade C")
else:
    print("fail")

#ask the user to input the month number(1 to 12)
# and print the season
# winter:dec-feb
#spring:mar-may
# summer:Jun-aug 
# Autumn: sept- Nov
#  
month=int(input("Enter the month number"))
if month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
elif month in [12,1,2]:
    print("Winter")
else:
    print("ERROR")

#ASK THE USER TO ENTER A SINGLE ALPHABET AND CHECK IF IT IS
# A VOWEL OR A CONSONANT
# VERY IMPORTANT QUESTION

alphabet=input("enter a single alphabet")
if alphabet in ["a","e","i","o","u"]:
    print("VOWEL")
else:
    print("Consonant")

# ask the user for a mark(0 to 100).
# If it is 40 or above, print pass else print fail
mark=int(input("Enter your marks"))
if mark>=40:
    print("PASS")
else:
    print("Fail")

# ask the user to enter a number and check if its divisible by 3 and 5
num=int(input("enter a number"))
if num%3==0 and num%5==0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")

#ask the user their age and print
# child (age<13)
# teenager(13 to 19)
# adult(20-59)
# senior(60 and above)

age=int(input("Enter your age"))
if age<13:
    print("Child")
elif 13<=age<=19:
    print("Adult")
elif 20<=age<=59:
    print("Adult")
elif age>=60:
    print("Senior")
else:
    print("ERROR")

# Ask the user to enter three numbers from the user and 
# print the greatest among them

A=int(input("Enter a number"))
B=int(input("Enter a number"))
C=int(input("Enter a number"))
if A>B and A>C:
    print("A is greater")
elif B>A and B>C:
    print("B is greater")
else:
    print("C is greater")

# ask the user to enter two numbers and an operator(+,-,*,/)
# and perform the calculation 

num1=int(input("number1"))
num2=int(input("number2"))
operator=input("an operator")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("ERROR")
