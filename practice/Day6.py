#try:
#    age=int(input("enter your age"))
#    print("your age is",age)
#except:
#    print("Please enter numbers only")


try:
    number=int(input("enter the number"))
    result=10/number
    print("Result is",result)
except:
    print("something went wrong")

cart={"apple":30,"banana":20,"milk":50}
#ask the users to enter an item name.
# show the price
# handle the case when an item doesnt exist in the cart.
try:
    cart={"apple":30,"banana":20,"milk":50}
    itemName=input("an item name ").lower()
    print(f"The price of {itemName} is {cart[itemName]}")
except:
    print("Sorry,The item is not in the list")


# 1. Print all numbers from 1 to 100 using a for loop
for i in range(1,101):
    print(i)
    i+=1

# 2.Print the multiplication table of a number entered by the user
N=0
num=int(input("Enter a number to find its multiplication table"))

for i in range(1,11):
    N=i*num
    print(N)
    i+=1

# 3.Calculate the factorial of a number using a while loop
num=int(input("Enter a number to find its factorial value"))
Ans=1
i=num
while i>0:
    Ans=Ans*i
    i-=1
print(f"The value of {num}! is {Ans}")

# 4.Print all the numbers between 1 and 50

i=1
while i<=50:
    if i%2==0:
        print(i)
        i+=1
    else:
        i+=1

# 5.fIND THE SUM OF DIGITS OF A NUMBER(E.G., 123 --> 1+2+3=6)
num=int(input("enter a number to find its sum of digits"))
i=1

while i>0:
    if num < 10**i:
        break
    else:
        i+=1
i-=1
N=num
a=0
sum=0
while i>=0:
    a=N//(10**i)
    N-=a*(10**i)
    sum+=a
    i-=1
print(f"The sum of digits of {num} is {sum}")


# 6.Write the function that takes a number and returns if its prime

num=int(input("Enter a number to check if its a prime number"))
if num<=1:
    print(f"The number {num} is not a prime number")
else:
    i=2
    while i<(num+1)/2:
        if num%i==0:
            print(f"The number {num} is not a prime number")
            break
        else:
            i+=1
        print(f"The number {num} is a prime number")
        break

# 7.Write a function thatr calculates the area of a circle(radius as input)

radius=0
Area=0
def CircleArea(radius):
    Area=(3.14*(radius**2))
    return Area

print(CircleArea(2))

# 8.Write a function that accepts two numbers 
# and returns their greatest common divisor

n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
if n1<n2:
    N=n1
else:
    N=n2
gcd=0

for n in range(2,N+1):
    if n1%n==0 and n2%n==0:
        if gcd<n:
            gcd=n
        else:
            break
    else:
        n+=1
print(gcd)

# 9.Write a function that counts how many vowels are in a string
string=input("Enter a string")
vowels=["a","e","i","o","u"]
counter=0
for i in range(len(string)):
    if string[i] in vowels:
        counter+=1
    else:
        i+=1
print(counter)

# 10. Write a function to reverse a string
#(e.g., "hello"-->"olleh")

string=input("Enter a string to reverse")
l=int(len(string))
reverse=[]
i=l-1
while i>=0:
    reverse.append(string[i])
    i-=1
separator=""
print(separator.join(reverse))

# 11.Write a program that devides two numbers and handles division by zero

try:
    n1=int(input("first number"))
    n2=int(input("second number"))
    div=n1/n2
    print(div)
except:
    print("You cannot divide a number by zero. Try Again.")

#12. ask the user to enter their age. 
#Handle the case where they type text instead of a number

try:
    age=int(input("Enter your age"))
except:
    print("Error. You entered a text, instead of a number")
