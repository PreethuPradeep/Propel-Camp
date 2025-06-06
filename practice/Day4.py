#important question
#1. compare lists tuples and dictionaries based on
#   a. mutability
#   2. syntax
#   3. use case
#2. when would you use a dictionary instead of a list or atuple?



a=10
b=5

print(a>b)#true
print(a<b)#false as 10 is not less than 5
print(a==b)#false as 10 is not equal to 5
print(a!=b)#true as 10 is not equal to 5
print(a>=b)#true as 10 is greater than 5
print(a<=b)#false as 10 is not less than or equal to 5


#Logical Operators

#AND - Noth conditions must be true
#OR -At least one condition must be true
#NOR -Reverses the condition that means true becomes false and vice-versa

a=10
b=5
c=20

#Logical AND

print(a>b and c>a)#true

#Logical OR
print(a<b or c>a) #true

#Logical NOR
print(not a>b) # not(true) -> false

#expresssions


#1. constant expressions

x=15+1.3
print(x)

#2. arithmetic expressions



x=40
y=12
add=x+y
sub=x-y
pro=x*y
div=x/y

#3. Integral expressions produce only integer results after all computations

a=13
b=12.0
c=a+int(b)
print(c)

#4. Floating expressions
#produce floating point numbers as result
a=13
b=5
c=a/b
print(c)

#5. relational expressions: arithmetic expressions are written on both sides of relational operators
a=21
b=13
c=40
d=37
p=(a+b)>=(c-d)

#6. Logical expressions: These are kinds of expressions 
# that result in either True or False

p=(10==9)
q=(7>5)
#Logical expressions
R=p and q
s=p or q
t=not p
print(R)
print(s)
print(t)

#user input
#name=input("enter the name")
#print("hello",name)

#age=int(input("enter the age"))
#print("your age is",age)

#write a program to take two numbers from the user and print their sum

a=int(input("enter a number"))
b=int(input("enter a number"))
sum=a+b
print(sum)

# write a program to take two numbers as input and print the product

product=a*b
print(product)
# Ask the user for their fist and last name and print their full name

first_name=input("enter the first name")
last_name=input("enter the last name")
name=(first_name,last_name)
separator=" "
print(separator.join(name))

# Ask the user for the radius of a circle and calculate the area

radius=int(input("enter a value"))
area=3.14*(radius**2)
print(area)

# take a string and a number from the user and print that string many times

string=input("enter a string")
number=int(input("enter a number"))
print(string*number)








