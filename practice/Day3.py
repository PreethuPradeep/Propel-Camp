
fruit_prices={
    "apple":2.5,
    "banana":1.2,
    "orange":3.0,
    "mango":4.5
              }

#access the price of orange
print("price of orange\t",fruit_prices["orange"])

#add a new fruit
fruit_prices["grapes"]=2.8
print(fruit_prices)

#update price of banana
fruit_prices["banana"]=2.5

#remove an element
del fruit_prices["mango"]

#get(): Return sthe value of given key
print(fruit_prices.get("banana"))

#items():Returns a list of dictionary's pairs as tuples
print(fruit_prices.items())

#Keys(: It returns a list of dictionary's keys
print(fruit_prices.keys())

#value(): returns a list of dictionary's values
print(mystudents.values())

#len():find the no of items in a dictionary
print(len(fruit_prices))

#clear(): deletes all items in the dictionary
fruit_prices.clear()
print(fruit_prices)

#del: deletes the entire dictionary
del fruit_prices
#print(fruit_prices)

#problems
#Qn1    Creates a dictionary called cities with the following data:
#       "Chennai":"Tamil Nadu",
#       "Mumbai":"Maharashtra",
#       "Bengaluru":"Karnataka"

mydict={"Chennai":"Tamil Nadu","Mumbai":"Maharashtra","Bengaluru":"Karnataka"}
#Qn2    print the state of "Mumbai"
print(mydict["Mumbai"])

#qn3    Check if "Delhi" is in the dictionary. If not add "Delhi":"Delhi"
#       to the dictionary
print("Delhi" in mydict)
mydict["Delhi"]="Delhi"
print(mydict)

#qn4    change "Mumbai"'s value to "Maharashtra(West India)"
mydict["Mumbai"]="Maharashtra(West India)"

#qn5    print all cities names
print(mydict.keys())

#qn6    print all states names
print(mydict.values())

#qn7    print all the city state pairs
print(mydict.items())

#qn8    print how maany cities are in the dictionary
print(len(mydict))





