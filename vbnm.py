import random
myList = []
unique_list = []
"""
function explanation: Runs all of the code.
"""
def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("please choose from the following options.   Type the number of the choice")
        choice = input("""1. Add to a list,
2, Add a bunch of numbers,
3. Get an item at an index
4. Sort list
5. Random search
6. Linear search
7. Recursive Binary Search
8. Iterative Binary search
9. Print list
10. Quit   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            addABunch()
        elif choice == "3":
           indexValues()
        elif choice == "4":
            sortList(myList)
        elif choice == "5":
            randomSearch()
        elif choice == "6":
            linearSearch
        elif choice == "7":
            binSearch = input("What number are you looking for?  ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        elif choice == "8":
            binSearch = input("What number are you looking for?  ")
            result = iterativeBinarySearch(unique_list, int(binSearch))
            if result != -1:
                print("Your number is at index position {}".format(result))
            else:
                print("Your number is not found in that list,  bud!")

        elif choice =="9":
                printLists()
            
        else:
                break
"""
function explanaton:Adds to a list.
"""

def addToList():
    print("adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors
"""
function explanation: adds to a list.
"""

def addABunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("How many new integers would you like to add?   ")
    numRange = input("And how high would you like the numbers to go?   ")
    for x in range (0,   int(numToAdd)):
        myList.append(random.randint(0,  int(numRange)))
    print("your list is complete!")
"""
function explanation: Sorts a list.
"""

def sortList(myList):
    #note that this is the first function we've built here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new,  sorted list?  Y/N")
    if showMe.lower() =="y":
        print(unique_list)
"""
function explanation: Print im so random.
"""

def randomSearch():
    print("oH iM sO rAnDom!!!")
    print(myList[random.randint(0,  len(myList)-1)])
    if len(unique_list[random.randint(0, len(unique_list)-1)]

def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int (searchValue):
            print("Your item is at index position()".format(x))


def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("You number is at index position()".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isn't here!") 

"""
Function explanation: We created a variable called 'index pos', and stored
the result of an input function inside it.

We then force the value stored in index pos ino an integer (using the int() function)
and used that variable to call a value at a specific index position.
"""

"""
Function explanaion. Makes a print value.
"""

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(mtList[int(indexPos)])

"""
Function explanation: Makes a list of numbers or letters.
"""
def printLists():
    if len(unique_list) == 0:
        print(myLIst)
    else:
        whichOne = input ("Which list do you want to see? Sorted or un-sorted?  ")
        if whichOne.lower() == "sorted":
            print (unique_list)

""" 
Function explanation: Makes a high and low list.
"""


def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif inuque_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    mainProgram()
    



