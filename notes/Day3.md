Dictionary

    Dictionary is a collection of related data pairs
    dictionaryname={dictionaryKey:data}
    dictionary keys must be unique in one dictionary.

    if we want to store the name and age of students.
    mystudents is the dictionary name

        mystudents={"Abhi":30,"sibi":28,"subi":"not updated"}

    access the price of orange
        print("price of orange\t",fruit_prices["orange"])

    add a new fruit
        fruit_prices["grapes"]=2.8
        print(fruit_prices)

    update price of banana


    remove an element
        del fruit_prices["mango"]

    get(): Return sthe value of given key
        print(fruit_prices.get("banana"))

    items():Returns a list of dictionary's pairs as tuples
        print(fruit_prices.items())

    Keys(: It returns a list of dictionary's keys
        print(fruit_prices.keys())

    value(): returns a list of dictionary's values
        print(mystudents.values())

    len():find the no of items in a dictionary
        print(len(fruit_prices))

    clear(): deletes all items in the dictionary
        fruit_prices.clear()
        print(fruit_prices)

    del: deletes the entire dictionary
        del fruit_prices
        print(fruit_prices)
