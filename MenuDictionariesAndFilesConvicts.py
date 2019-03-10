#Program 3

from operator import itemgetter

def loadList(aList):
    snIn=open("Convict.txt","r")
    while True:
        dictionary={}
        
        dictionary["name"]=str.strip (snIn.readline())
        if dictionary["name"]=="":
            break
        dictionary["prisonerNumber"]=str.strip(snIn.readline())
        dictionary["crime"]=str.strip (snIn.readline())
        dictionary["yearsSentenced"]=int(str.strip(snIn.readline()))
        dictionary["parol"]=dictionary["yearsSentenced"]*.66
        
        aList.append(dictionary)

def dangerous (aList):
    snOut=open("Dangerous.txt","w")
    print("List of Prisoners sentenced to more than 10 years:")
    for elem in aList:
        if elem["yearsSentenced"] > 10:
            print(elem["name"],elem["prisonerNumber"])
            snOut.write(elem["name"]+"\n")
            snOut.write(elem["prisonerNumber"]+"\n")  
    snOut.close()

def seeInfo (aList):
    check = False
    name=str(input("Input a convicts name to see their information "))
    for elem in aList:
        if name==elem["name"]:
            print("Name:",elem["name"])
            print("Prisoner Number:",elem["prisonerNumber"])
            print("Crime:",elem["crime"])
            print("Years Sentenced:",elem["yearsSentenced"])
            print("Parol Years:",elem["parol"])
            check = True
    if check == False:
        print("That convict is not in our records")

def longestSentence (aList):
    check = 0
    for elem in aList:
        if elem["yearsSentenced"]=="":
            break
    
        elif elem["yearsSentenced"] > check:
            check = elem["yearsSentenced"]
            name = elem["name"]
        else:
            continue
    print (name,"has the longest sentence of",check,"years")

def average (aList):
    total=0
    numberOfConvicts=len(aList)
    for elem in aList:
        total += elem["yearsSentenced"]
    final=round(total/numberOfConvicts,2)
    print(final,"is the average number of years sentenced")

def tableLongestToShortestSentence(aList):
    bList=[]
    bList [ : ]= aList
    bList.sort(key = itemgetter ("yearsSentenced"))
    print("Name:".rjust(18),"Crime:".rjust(18),"Years Sentenced:".rjust(20))
    print()
    for elem in bList:
        print(elem["name"].rjust(18),elem["crime"].rjust(20),str(elem["yearsSentenced"]).rjust(15))
  
#Menu

def showMenu ():
    print ()
    print ("Choose an item from the list: ")
    print ()
    print ("1. More than 10 yrs")
    print ("2. Input convicts name, see info")
    print ("3. Longest Sentence")
    print ("4. Average")
    print ("5. Table")
    print ("6. End")
    print ()

#Mainline

aList=[]
loadList(aList)
while True:
    
    showMenu()
    userChoice = input ("Enter a menu choice: ")

    if userChoice == "1":
        dangerous (aList)
    elif userChoice == "2":
        seeInfo (aList)
    elif userChoice == "3":
        longestSentence (aList)
    elif userChoice == "4":
        average (aList)
    elif userChoice == "5":
        tableLongestToShortestSentence(aList)
    elif userChoice == "6":
        break
    else:
        print ("Input a choice between 1 and 6 pls")

snIn.close()
print ("Program done")
