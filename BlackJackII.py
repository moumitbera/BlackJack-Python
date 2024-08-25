#blackjack 2.0
#author: @moumit

import art
import random
import os

#finite deck case = if a card is drawn that card would not show up again

#implementing code for ease
#100 = win
#101 = lost as the number exceeds 21
#102 = lost as computer scored higher
#103 = draw
#104 = won as computer exceeds 21

# Game details
deck = ["ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
valueDict = {
    "ace": 11,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
}

outputMessages = {
    100: "You won!",
    101: "The total of your cards exceeds 21. You lost.",
    102: "Dealer scored higher. You lost.",
    103: "Dealer and you both have the same score. It's a draw",
    104: "You won! The total of dealer's cards exceeds 21",
    105: "error",
}

wantToPlay = input("Do you want to play blackjack? Type y for yes and n for no \n").lower()
if wantToPlay == "y":
    continuePlaying = True
else:
    continuePlaying = False



def clearTerm():
    os.system("cls")

def check(uScore, cScore):
    if cScore < 21 and uScore < 21:
        if cScore == uScore:
            return 103
        elif uScore > cScore:
            return 100
        elif uScore < cScore:
            return 102
        else:
            return 105
    else: 
        if uScore > 21:
            return 101
        elif cScore > 21:
            return 104
        else:
            return 105
    





def selectCard(num, scoreOf, cardOf):
    '''
    requires input to determine the number of cards to be generated randomly. Further, calculates score
    and gives the final score and card list
    '''
    for i in range(num):
        cardSelected = random.choice(deck)
        if cardSelected == "ace":
            if scoreOf + 11 > 21:
                valueDict["ace"] = 1
        scoreOf = scoreOf + valueDict[cardSelected]
        cardOf.append(cardSelected)
        deck.remove(cardSelected)
    return scoreOf

def wantAnotherCard():
    wantAnotherCard = input("Do you want to draw another card? Y for yes, N for no\n").lower()
    if wantAnotherCard == "y":
        return True
    else:
        return False


def game():
    userScore = 0
    computerScore = 0
    userCards = []
    computerCards = []

    print(art.logo)
    
    print("Welcome to backjack.")
    
    userScore = selectCard(2, userScore, userCards)

    print(f"Your cards are {userCards} scoring {userScore}")
    
    computerScore = selectCard(2, computerScore, computerCards)
    print(f"Dealer's first card is [{computerCards[0]}, x] scoring {valueDict[computerCards[0]]}")

    if computerScore == 21 or userScore == 21: #checking for blackjack
        if computerScore == 21:
            print("You lost")
            print(f"Dealer has got a blackjack, with cards {computerCards}.")
        elif userScore == 21:
            print(outputMessages[100])
            print(f"You have got a blackjack, with cards {userCards}")
    else:

        if computerScore < 17:
            computerScore = selectCard(1, computerScore, computerCards)
        
        while wantAnotherCard():
            userScore = selectCard(1, userScore, userCards)
            print(f"Your updated cards are {userCards} scoring {userScore}")
            if userScore > 21:
                print(outputMessages[101])
                break
            
        print("\nSummary:")
        print(f"Your final cards are {userCards}, scoring {userScore}")
        print(f"Dealer's final cards are {computerCards}, scoring {computerScore}")
        
        print(outputMessages[check(uScore=userScore, cScore=computerScore)])
        
    wantToPlayAgain = input("Do you want to play again? Y for yes & N for no\n").lower()
    if wantToPlayAgain == "y":
        clearTerm()
        game()
    else:
        print("Thanks for playing!")
        
game()
