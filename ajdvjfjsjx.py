import random
myList = []

def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("please choose from the following options.   Type the number of the choice")
        choice = input("""1. Add to a list,
2, Return a value in a list,
3. Add a bunch of numbers
4. Random Search
5. Linear search
6. Print List
7. Quit   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            print(myList)
        else:
                break

def addToList():
    print("adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors


def addABunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("How many new integers would you like to add?   ")
    numRange = input("And how high would you like the numbers to go?   ")
    for x in range (0,   int(numToAdd)):
        myList.append(random.randint(0,  int(numRange)))
    print("your list is complete!")
        


def randomSearch():
    print("oH iM sO rAnDom!!!")
    print(myList[random.randint(0,  len(myList)-1)])

def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int (searchValue):
            print("Your item is at index position()".format(x))

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(mtList[int(indexPos)])



if __name__ == "__main__":
    mainProgram()
    



