#Ryan Kinsella
#Lists 11
#User inputs the number of rows and columns they like to have
#User inputs a series of numbers to be in the table
#The output is the the table

twoDList = []

col = []

rowNumB = int(input("How many rows? "))
colNumB = int(input("How many columns? "))

for rowNumA in range (0,rowNumB):
    row = []
    
    for colNumA in range (0, colNumB):
        row.append ( int(input("Input a number for the column ")) )
    twoDList.append (row)



print ("The table is:")

for rowNumA in range (0, rowNumB):
    for colNumA in range (0, colNumB):
        print (str(twoDList[rowNumA][colNumA]).rjust(3), end = "")
    print ()

#alternative way to do ^
# def dealDeckIntoStacks(): #list, int, int, returns void
#     #Create a 2-Dimensional list called piles.
#     #The first index set is one of four piles for each suit (hearts, etc...)
#     #The second index set is the amount of cards per pile, with each index containing a card
#
#     deckIndex=0
#     global stacks
#     global deck
#     for i in range (0,n): #for each pile
#         pile=[]
#         for j in range (0,m): #for the amount of cards per pile
#             pile.append(deck[deckIndex])
#             deckIndex += 1
#         print("test")
#         stacks.append(pile)
