# Higher Or Lower Game
import random


# Playing Card Constants
SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8


# Go through the deck and pick a random card
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard


# Go through the deck and shuffle the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


# Main Game Code
print("Welcome to Higher or Lower")
print("You will have to choose weather the next card is higher or lower than the current card")
print('Getting it right adds 20 points to your score, getting it wrong subtracts 15 points')
print('You start with 50 points')
print()

startingDeckList = []
for suit in SUITS:
    for thisValue, rank in enumerate(RANKS):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50


while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('The starting card is:', currentCardRank + ' of' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('The next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Correct!')
                score += 20
            else:
                print('Wrong!')
                score -= 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score += 20
                print('You got it right!')
            else:
                score -= 15
                print('You got it wrong!')
        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('Do you want to play again? (Press ENTER or q): ')
    if goAgain == 'q':
        break

print('Thanks for playing!')
