message="Hello World!"
print(message)

my_money=100
print(my_money)

my_balance=1000.0
print(my_balance)

#multiple assignment
num1=num2=num3=200
print(num1)
print(num2)
print(num3)

name="Preethu"
age="26"
city="Trivandrum"

print(name)
print(age)
print(city)

#calculate the area of a rectangle
l=10
b=5
area=l*b
print(area)

#qn3: Given two numbers, find the sum,difference,product and quotient
num1=10
num2=5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#qn4: calculate the total cost, if given price and quantity
price=199.99
quantity=3
total_cost=price*quantity
print(total_cost)

#qn5: Create a variable, temparature in celcius,
#calculate the temp in faranheit
#using the equation f = c*9/5 + 32
temp_in_celcius=27
temp_in_faranheit=temp_in_celcius*9/5 + 32
print(temp_in_faranheit)

#qn6: Create a simple program to store various details of a student
# print them
name= "Anna"
role_no="27"
semester="s4"
department="civil"
phone_no="936788998"
email_address="annamathew@gmail.com"

print("Name:",name)
print("role no:",role_no)
print("Semester:",semester)
print("Department:",department)
print("Phone No:",phone_no)
print("Email Address:",email_address)

A=10
B=5
print(A,B)
del A
print(B)

#TYPE CONVERSION
int_eg=100
float_eg=3.14

#converting into to float
print(float(int_eg))
#converting float into int
print(int(float_eg))
#converting int to string
print(str(int_eg))

#you have an integer 10 & a string "20"
# convert the string into an integer and print the sum
integer=10
string="20"
integer2=int(string)
print(integer+integer2)

#convert the integer 30 into a string and print the result
integer=30
string=str(integer)
print(string)

#arithmetic operations in python

a=10
b=3

print("Addition:",a+b)
print("substraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:", a//b)#rounds to the nearest( no decimal)
print("modulus:",a%b)#to find the reminder
print("exponent:",a**b)

A=10
B=5
#find the value of N=(a+b)^2
N= A**2 + 2*A*B + B**2
print(N)

name="abraham lincoln"
 
 #convertsthe first letter of each word to upper case
print(name.title())
 #convert the string to upper case
print(name.upper())
 #converts the string to lower case
print(name.lower())

#to add a tab to your text, use charecter \t
print("Apples\tOranges")

#to add a new line \n
print("Apples\nOranges")

#rstrip() removes white space from right end
#lstrip() removes white strip from left end
#strip() removes white strip from both ends
fruits = " Apples and Oranges  "
print(fruits)
print(fruits.lstrip())
print(fruits.rstrip())
print(fruits.strip())

#Declare a variable price= "299.99" Convert it into float and print
price = "299.99"
print(float(price))
#Convert total seconds into minutes and Seconds t=125 sec
total_secs = 125
mins = total_secs//60
secs= total_secs%60
print(mins,"mins and", secs,"secs")
#Convert a float value 45.8 into an integer and print
n=45.8
print(int(n))
#Calculate the area of a cicle
r=3.5
area=3.14*(r**2)
print(area)
#Calculate simple interest SI = (P*R*T)/100
P=1000
R=5
T=2
SI = P*R*T/100
print(SI)
