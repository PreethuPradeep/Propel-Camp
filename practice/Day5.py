
#We have a list named fruit
fruits=["Apples", "Oranges", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)


#print all integers multiples of 5 less than 50
for i in range(0,50,5):
    print(i)

#print only the even numbers from the list
#numbers=[12,3,7,14,10,5]

numbers=[12,3,7,14,10,5]
for num in numbers:
    if num%2==0:
        print(num)


score=[50,60,70,80]
#add 10 to each number on the list and print the list
for i in score:
    print(i+10)

for i in range(len(score)):
    score[i]+=10
print(score)


#print() numbers from 1 to 5 using while loop
counter=1
while counter<=5:#stops when the counter becomes 6
    print(counter)
    counter+=1# increases the counter by one each value

#write a program that prints a number from 1 to 20 using while loop
i=1
while i<=20:
    print(i)
    i+=1

#print all even numbers from 0 to 20 using while loop

i=2
while i<=20:
    if i%2==0:
        print(i)
    i+=1

i=2
while i<=20:
    print(i)
    i+=2
# use a while loop to count down from 10 to 1 then print "GO"

i=10
while i>=1:
    print(i)
    i-=1
print("GO")

#Keep asking the user to type the password "password123" till they get it right.


Password=input("PLEASE ENTER THE PASSWORD:  ")
if Password =="Password123":
    print("Correct Password")
else:
    print("Access Denied. Wrong Password.")

# Secret number is 9. Ask the user to guess till they get it right

i=0
while i<=9:
    print(i)
    i+=1


# Print each letter in the word "banana"

word="banana"
for i in range(len(word)):
    print(word[i])
    i+=1

# Write a program to swap two variables

v1=input("Variable1")
v2=input("Variable2")
temp=v1
v1=v2
v2=temp
print("After swapping")
print("v1=",v1)
print("v2=",v2)


# Write a program to check if the number is prime or not
#prime number
#greater than1 that is divisible by 1 and itself

#input from user
num=int(input("Enter a number"))

#if the number is 1 or less, then its not prime
if num<=1:
    print("its not prime")
else:
    n=int((num+1)/2)
    for i in range(2,n):
        if num%i==0:
            print("not a prime number")
            break#break stops the loop if we find such a number
        else:
            print("prime")

# Write a program to find the maximum number in a list
list=[1,2,3,4,5,6,7]
for i in range(len(list)):
    if list[i]>:
        N=list[i]
        i+=1
        if N>list[i+1+1]:

    else:
        N=list[i+1]
    

# Write a program to find the minimum number in a list
# Write a program to find the middle element in a list

#Break Statement


for num in range(1,10):
    if num==5:
        break
    print(num)

# Continue Statement


for num in range(1,6):
    if num==3:
        continue# skip the number
    print(num)

# Function

# Function to add two numbers

def findSum(a,b):
    sum=a+b
    return sum

findSum(12,4)# calling the function

#function to check if number is even or odd
#defining the function

def check_even_odd(number):
    if num%2==0:
        print("even")
    else:
        print("odd")

check_even_odd(7)


#function to find thelargest of two numbers
#without and with user input

def largestNum(a,b):
    if a>b:
        print("a is largest")
    else:
        print("b is largest")

largestNum(23,16)
a=int(input("num1"))
b=int(input("num2"))
largestNum(a,b)

message="I am a global variable"
def myfUNCT():
    #DECLARING A LOCAL VARIABLE
    message2="I am a  local variable"
    print(message2)

myfUNCT()
#print(message2)#NameError: name 
# 'message2' is not defined.

#create a function that declares a local variable x=10 and prints it.
#also try printing x outside the function what happens?

def localvar(y):
    x=10
    sum=x+y
    return sum
localvar(9)
print(x)
