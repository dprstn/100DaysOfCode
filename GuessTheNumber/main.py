import random
import pyinputplus as pyip
from art import logo


def DisplayPrompt(Desc, LowestNum, HighestNum):
    print(Desc)
    return pyip.inputNum(prompt='Make a guess: ', min=LowestNum, max=HighestNum)


def Difficulty():
    return 5 if pyip.inputYesNo(prompt='Choose hard or easy: ', yesVal='Hard',
                                noVal='Easy').lower() == 'hard' else 10


def PlayGame():
    print(logo)
    Guesses = Difficulty()
    NumberToGuess = random.randint(1, 100)
    LowestGuess = 1
    HighestGuess = 100
    GameOver = False

    while not GameOver:
        print(f"The Number is between {LowestGuess} and {HighestGuess}")
        print(f'pssst number to guess is {NumberToGuess}')
        NumGuess = DisplayPrompt(Desc=f'You have {Guesses} attempts remaining to guess the number.',
                                 LowestNum=LowestGuess,
                                 HighestNum=HighestGuess)
        if NumGuess < NumberToGuess:
            print('Too low.\nGuess Again.')
            LowestGuess = NumGuess
        elif NumGuess > NumberToGuess:
            print('Too High.\nGuess Again.')
            HighestGuess = NumGuess
        else:
            print(f'You Got it Right.. the Number was {NumberToGuess}')

        Guesses -= 1
        if Guesses == 0 or NumGuess == NumberToGuess:
            if pyip.inputYesNo(prompt='Do You Want To Play Again: ').title() == 'Yes':
                return PlayGame()
            else:
                GameOver = True


PlayGame()
