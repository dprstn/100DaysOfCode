import random
from art import logo
import pyinputplus as pyip

LISTS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def DealCard():
    return random.choice(LISTS)

def DisplayFirstHand():
    print(f"Your Cards:{PlayerList}, current score: {PlayerScore}\n"
          f"Computer's first hand: {ComputerList[0]}")

def DisplayFinalHand():
    print(f"Your final hand: {PlayerList}, final score: {PlayerScore}\n"
          f"Computer's final hand: {ComputerList}, final score: {ComputerScore}")

def CompareScore():
    if ComputerScore == PlayerScore or ComputerScore > 21 and PlayerScore > 21:
        print('Its a Draw!')
    elif PlayerScore > 21:
        print('You went Over... Computer Won!')
    elif ComputerScore > 21:
        print('Computer went Over... You Won!')
    elif PlayerScore > ComputerScore:
        print('Player Won!')
    else:
        print('Computer Won!')

def Sum(CardDeck):
    if len(CardDeck) == 0:
        return 0
    return CardDeck[0] + Sum(CardDeck[1:])

def CheckIfAce(CardDeck):
    Score = Sum(CardDeck)

    if 11 in CardDeck and Score > 21:
        CardDeck.remove(11)
        CardDeck.append(1)
        return Sum(CardDeck)
    return Score

while pyip.inputYesNo('Do you want to play a game of BlackJack? ').title() == 'Yes':
    print(logo)
    ComputerList = []
    PlayerList = []
    ComputerScore = 0
    PlayerScore = 0
    ComputerList.append(DealCard())
    ComputerList.append(DealCard())
    PlayerList.append(DealCard())
    PlayerList.append(DealCard())
    PlayerScore = CheckIfAce(PlayerList)
    ComputerScore = CheckIfAce(ComputerList)
    DisplayFirstHand()
    prompt = pyip.inputYesNo("Type 'Yes' to get another card, type 'No' to pass: ").title()
    while prompt == 'Yes':
        PlayerList.append(DealCard())
        PlayerScore = CheckIfAce(PlayerList)

        if PlayerScore > 21:
            DisplayFinalHand()
            CompareScore()
            break
        else:
            DisplayFirstHand()
            prompt = pyip.inputYesNo("Type 'Yes' to get another card, type 'No' to pass: ").title()

    if prompt == 'No':
        while PlayerScore > ComputerScore and ComputerScore < 17:
            ComputerList.append(DealCard())
        ComputerScore = CheckIfAce(ComputerList)
        DisplayFinalHand()
        CompareScore()
