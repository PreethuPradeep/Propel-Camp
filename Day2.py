#Day 2
#string slicing

greet="Good Morning"
print(greet)
print(greet[0])#first character
print(greet[2:5])#charectors from 2 to 5-1
print(greet[2:])#characters from 3 onwards
print(greet*2)# types greet two times
print(greet+"WORLD")# CONCATENATED string

#Qn1
message="python is fun"
print(message)
print(message[1])
print(message[:6])
print(message[8:])
print(message*3)
print(message+" Let's learn")

#count method: returns the number of times the
#substring appear in the string

#count the entire string
print("Hello Good Morning".count("d"))

#count from index 3 to the end of string
print("Hello, Good Morning".count("d",3))

#endswith-return true if the string ends
#with the specified suffix

print("Superman".endswith("man"))# true

#check from index 3 to end of string
print("Superman".endswith(("man",3)))

#check from index 2 to 6-1
print("Superman".endswith("man",2,6)) #false

#isalnum()returns true if all characters in a string are alphanumeric
#alphanumeric(combination of alphabets and numbers and no spaces)
print("Hello1234".isalnum())
print("h e l l o 1 234".isalnum())
print("Hello World".isalnum())
print("HelloWorld".isalnum())

#isalpha() checks if the strings are only aphabets, no spces, numbers or 
# symbols.
print("Hello".isalpha())
print("Hello123".isalpha())
print("Hello World".isalpha())
print("python!".isalpha())

#isdigit() checks if all characters in a string 
# are digits(numbers)

print("12345".isdigit())#true
print("007".isdigit())#true
print("12abc".isdigit())#false

#islower() checks if all letters are lowercase.
print("hello".islower())#true
print("Hello".islower())#false
print("123abc".islower())#true(numbers are ignored, only checks letters)

#isupper() checks if all letters are uppercase
print("HELLO".isupper())#true
print("Hello".isupper())#false

#join()
separator=" "
myTupule=("h","e","l","l","o")
print(separator.join(myTupule))


#replace() is used to replace a part of  a string with something else.
#string.replace(old,new)
print("Hello World".replace("o","i"))

#len() to get the length(number of charecters)
text="Hello"
print(len(text))

#qn1
t1="Animals"
t2="Badger"
t3="Honey Bee"
t4="Honey badger"


print(t1.lower())
print(t2.lower())
print(t3.lower())
print(t4.lower())

#qn2


print(t1.upper())
print(t2.upper())
print(t3.upper())
print(t4.upper())

#qn3
string1="   Fillet Mignon"
string2="Brisket    "
string3=" cheeseburger  "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

#qn4
string1 = "Becomes"
string2="becomes"
string3="BEAR"
string4="   beautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

#qn5
string1= string1.lower()
string3= string3.lower()
string4=string4.lstrip()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

#Problem3
#qn1
name="hjgfaskdhg"
print(len(name))

#qn2
nmae2="hgdhlajf"
print(name+nmae2)

#LISTS
#Collection of data which are normally
#  related instead of stored as separate variables

students_age=[18,21,23,20,21]
print(students_age)
print(students_age[0])#prints first item on the list
print(students_age[-1])#prints the last item on the list
print(students_age[2:4])#slice part of list from 2 to 4-1
print(students_age[:4])#slice into a list till 4-1

#inserting an element
#insert a new element to the list using .append()
students_age.append(30)
print(students_age)

#inserting an element at a specific position
students_age.insert(2,45)
print(students_age)

#removing a specific element
students_age.remove(30)
#removing an element from the end
students_age.pop()
print(students_age)

#len: to find the number of items ina list
print(len(students_age))

#in: it checks if an item is in a list
my_list1=["h","e","l","l","o"]
print("e" in my_list1)

#combine two list
my_list2=[1,2,3,4]
my_list1.extend(my_list2)
print(my_list1)

#reverse(): reverses the item in a list
my_list1.reverse()
print(my_list1)

#sort(): sort items alphabetically or numerically
my_list1=["h","e","l","l","o"]
my_list1.sort()
print(my_list1)

#concatenate a list
my_list1=["h","e","l","l","o"]
mylist2=["w","o","r","l","d"]
print(my_list1+mylist2)
#duplictae the list and concatenete it
print(my_list1*3)


#problem4
#qn1
fruits=["apple","banana","cherry","mango","orange"]
print(fruits)
#qn2
print(fruits[2])
#qn3
fruits[2]="grapes"
print(fruits)
#qn4
fruits.append("kiwi")
print(fruits)
#qn5
fruits.insert(1,"pineapple")
print(fruits)
#qn6
fruits.remove("banana")
print(fruits)
#qn7
print(fruits[:3])
#qn8
print("apple" in fruits)
#qn9
fruits.sort()
print(fruits)
#qn10
fruits.reverse()
print(fruits)


#Tuples
#tuples are like lists, but unlike lists we cannot modify their initial values
#we use () when declaring a tuple
months=("jan","feb","mar","apr")
print(months[0])
print(months[-1])

#we cannot modify it
#months[0]="dec"

myTuple=("hello","world",2022)

#len-number of elements in tuple
print(len(myTuple))

#in-checks if the item is in tuple
print('world' in myTuple)

#Tuples are immutable
#this means we can't add change or remove individual elements
#after the tuple is created
#but we can delete the whole tuple using the del keyword

#del myTuple
#print(myTuple)

#concatenation: addition operator
print(myTuple+('How','are','you'))

#multiplication operator:* duplicates the tuple and concatenate it.
print(myTuple*3)


#qn1:   create a tuple named languages  with values python, java, c++
#       print the tuple
languages=("python","java","c++")
print(languages)

#qn2:   devices=(laptop,tablet,smartphone,smartwatch)
#       print second element
#       print last element using negative indexing
devices=("laptop","tablet","smartphone","smartwatch")
print(devices[1])
print(devices[-1])

#qn3:   cities=(Mumbai,Delhi,Chennai,Kolkata)
#       check if Delhi is in the tuple
cities=("Mumbai","Delhi","Chennai","Kolkata")
print("Delhi" in cities)

#qn4:   sports=(cricket,football,hockey,tennis,badminton)
#       write code to print the number of items in the tuple
sports=("cricket","football","hockey","tennis","badminton")
print(len(sports))

#qn5:   create a tuple with the value python and repeat it four times
tuple=('python')
print(tuple*4)

#qn6:   delete the entire tuple
del tuple

#qn1:   create a tuple of 4 countries and print it
countries=('India', 'Pakisthan', 'Bangladesh', 'Nepal')
print(countries)

#qn2:   print second and last item
print(countries[1])
print(countries[-1])

#qn3:   print the first two items
print(countries[:2])

#qn4:   concatenate two tuples: one of numbers and one of fruits
numbers=(1,2,3,4) 
fruits=("apples","oranges")
print(numbers+fruits)

#qn5:   convert a list [1,2,3] to a tuple
myList=[1,2,3]
myTuple=tuple(myList)
print(myTuple)

#qn6:   Check if "India" is in the tuple
print("India" in countries)

#qn7:   Find the length of a tuple
print(len(countries))

#qn8:   Delete a tuple using del
del countries