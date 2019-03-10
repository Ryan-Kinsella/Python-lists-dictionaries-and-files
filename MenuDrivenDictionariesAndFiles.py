#Ryan Kinsella
#Lists and Dictionaries Test Review
#Program 2

from operator import itemgetter 

#Loads the list
def loadList (aList):
    snIn = open ("Overdue.txt", "r")
    while True:
        nary = {}

        nary["student"] = str.strip(snIn.readline ())
        if nary["student"] == "":
            break
        nary["grade"] = str(str.strip(snIn.readline ()))
        nary["book"] = str.strip(snIn.readline ())
        nary["days"] = int(str.strip(snIn.readline ()))
        nary["fine"] = int(nary["days"] * .5)

        aList.append (nary)

    snIn.close()

def updateFile (aList):
    snOut = open("Overdue.txt", "w")
    for elem in aList:
        snOut.write (str(elem["student"]) + "\n")
        snOut.write (str(elem["grade"]) + "\n")
        snOut.write (str(elem["book"]) + "\n")
        snOut.write (str(elem["days"]) + "\n")
    snOut.close()

def fromName (aList):
    check = False
    name = input ("Who would you like to see info on? ")
    for elem in aList:
        if name == elem["student"]:
            print (elem["student"],"in grade",elem["grade"],"with overdue book",elem["book"],"with",elem["days"],"days overdue owes",elem["fine"],"$")
            check = True
            
    if check == False:
        print ("That is not a student in the file")



def totalFines (aList):
    total =0
    print ()
    for elem in aList:
        total += elem["fine"]
    print (total, "is the total amount of fines for all the overdue books")

def table (aList):
    bList = []
    bList [ : ] = aList
    bList.sort(key = itemgetter ("student"))
    print ()
    for elem in bList:
        print ((str(elem["student"])).rjust(20),
               (str(elem["book"])).rjust(30),(str(elem["fine"])).rjust(5))

def vice (aList):
    snOut = open ("vp.txt", "w")
    for elem in aList:
        if elem["days"] > 10:
            print (elem["student"], "in grade",elem["grade"], "has an overdue book of", elem["days"],"days")
            snOut.write (str(elem["student"]) + "\n")
            snOut.write (str(elem["grade"]) + "\n")
            snOut.write (str(elem["book"]) + "\n")
            snOut.write (str(elem["days"]) + "\n")
    snOut.close()

def newStudent (aList):
    newbie = {}
    newbie["student"]=input ("Students name? ")
    newbie["grade"]=input ("Students grade? ")
    newbie["book"]=input ("Students book? ")
    newbie["days"]=int(input ("Students days overdue? "))
    newbie["fine"] = int(newbie["days"] * .5)
    aList.append (newbie)
    print ("Student added")

def doubleSortedTable (aList):
    bList = []
    bList [ : ] = aList
    bList.sort(key = itemgetter ("grade"))
    cList = []
    for elem in bList:
        if elem["grade"] == 9:
            print ("nu")
            
    
    print ()
    for elem in bList:
        print ((str(elem["student"])).rjust(20),(str(elem["book"])).rjust(30),(str(elem["fine"])).rjust(5))


#Menu
def showMenu ():
    print ()
    print ("Choose an item from the list: ")
    print ()
    print ("1. See a students name, grade, overdue book, and fine")
    print ("2. Total number of overdue fines")
    print ("3. Table of students names by alphebetical order")
    print ("4. Shows names and grade of students with overdue books of 10 days, sends to a file")
    print ("5. Adds a new student to the file")
    print ("6. Sorted by grade then by name in alphebetical order")
    print ("7. End Program")
    
    

#Main

aList = [] #Actual Parameter
loadList (aList)

while True:


    showMenu()
    print ()
    userChoice = input ("Enter a menu choice: ")

    if userChoice == "1":
        fromName (aList)
    elif userChoice == "2":
        totalFines (aList)
    elif userChoice == "3":
        table (aList)
    elif userChoice == "4":
        vice (aList)
    elif userChoice == "5":
        newStudent (aList)
    elif userChoice == "6":
        doubleSortedTable (aList)
    elif userChoice == "7":
        break
    else:

        print ("Input a choice between 1 and 6 please")
        
updateFile (aList)     
print ("Program done, Overdue.txt has been updated")
