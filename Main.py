import random
balance = 1000

#Draws Card
def drawCard():
    return(random.randint(1,21))

#Game Loop
activeGame = False

#Creates users card desk
userCard = []
#creates dealer card desk
dealerCard = []
while True:
    #menu
    print("Play")
    print("Balance")
    command  = input("Enter Function:")
    #play
    if (command == "Play"):
        activeGame = True
        while activeGame == True:
            
            #issue
            userCard.append(drawCard())
            userCard.append(drawCard())

            dealerCard.append(drawCard())
            dealerCard.append(drawCard())
            
            #count
            userValue = userCard[0] + userCard[1]
            
            dealerValue = userCard[0] + userCard[1]
            
            if (userValue > dealerValue):
                print("User Wins")
            else:
                print("Dealer Wins")
            print(f"User: {userValue}")
            print(f"Dealer: {dealerValue}")
            input()
            #Ends Game
            activeGame = False

