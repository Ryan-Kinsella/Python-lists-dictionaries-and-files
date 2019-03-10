#Ryan Kinsella

##    The User will make a menu driven program that will do the following:
##-   Output the words in the reverse order
##-   Output the words in alphabetical order while not changing the original list
##-   Allow the user to input a word and have the number of times the word appears in the list.
##-   Allow the user to input a word and have word removed from the list
##-   Allow the user to input two integers and have the “slice” of the list to be outputted
##-   Allow the user to input an integer and have the list “grow” that many times
##-   Output the “middle” word or words in the list after it has been outputted.
##-   Input a new set of words.
##-   Exit the program

import math

def loadList (listA):
    while True:
        
        word = input("Input a word ")
        listA.append (word)
        
        ans = input("Would you like to continue? (y or n) ")
        if ans == "n" or ans == "N":
            break
    
def reversedO (listA):
    for rev in reversed (listA):
        print (rev)

def alphebetical (listA):
    listA.sort()
    print (listA)

def occurences (listA):
    occur = input("What value of the list would you like to test? ")
    print (listA.count(occur), "is the number of times it appears in the list")
    
def delete (listA):
    while True:
        choice = input("Which item would you like to remove from the list? ")
        if listA.count(choice) == 0:
            print ("Input a valid choice")  
        else:
            listA.remove (choice)
            print ("Succesfully deleted")
            
        ans = input("Would you like to continue? (y or n) ")
        if ans == "n" or ans == "N":
            break
        
def elements (listA):

    choice = int(input("From which item would you like to view from the list? "))
    choiceA = choice - 1
    choiceB = int(input("To which item would you like to view from the list? "))
    for element in range (choiceA, choiceB):
        print ()
        print (listA [element])

def grow (listA):
    num = int (input("What magnitude would you like to grow the list? "))
    calulations = len (listA)
    listB = listA * num
    listA.append (listB)
    for element in range (1, calulations):
        listA.pop (element)

    print ()
    print (listA, "is the list")

        
def middle (listA):
    total = len(listA)
    mid = total % 2
    numA = total / 2
    numB = math.floor (num)
    numC = numA - 1
 
    if mid == 0:
        print ()
        print (listA [numC])
        print (listA [numB])           

    else:
        print ()
        print (listA [numB])

        
def newWords (listA):
    while True:
        
        word = input("Input a word ")
        listA.append (word)
        
        ans = input("Would you like to continue? (y or n) ")
        if ans == "n" or ans == "N":
            break


def showMenu():
    print ()
    print ("Enter a menu choice:")
    print ("1. Output list in reversed order")
    print ("2. Output 'words' in alphebetical order")
    print ("3. Number of times a word occurs")
    print ("4. Remove an item from the list")
    print ("5. Input two integers and have the “slice” of the list to be outputted")
    print ("6. Input an integer and have the list “grow” that many times")
    print ("7. Output the “middle” word or words in the list after it has been outputted")
    print ("8. Input a new set of words")
    print ("9. Exit Program")
    

#Mainline    

listA = []
loadList (listA)

while True:
    showMenu()
    print ()
    print (listA, "is your current list")
    print ()
    choice = input("Enter a menu choice ")

    if choice == "1":
        reversedO (listA)

    elif choice == "2":
        alphebetical (listA)

    elif choice == "3":
        occurences (listA)
        
    elif choice == "4":
        delete (listA)

    elif choice == "5":
        elements (listA)
        
    elif choice == "6":
        grow (listA)
        
    elif choice == "7":
        middle (listA)
        
    elif choice == "8":
        newWords (listA)

    elif choice == "9":
        break

    else:
        print ("Choose an option between 1 and 9 please:")

print ("Program done")


        
    
