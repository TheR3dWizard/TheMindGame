import random as r

cardlist = [i for i in range(1,101)]

numplayers = int(input("Enter number of players: "))
numrounds = int(input("Enter number of rounds (8,9,12): "))
finallist = []

for round in range(1,numrounds+1):
    print("Number of cards")
    numcards = round
    roundlist = []
    for player in range(numplayers):
        print('\n'*10000000)
        cards = []
        for i in range(numcards):
            card = r.choice(cardlist)
            cards.append(card)
            cardlist.remove(card)
        cards.sort()
        print(f"Player {player+1} has the following cards")
        input()
        print(cards,end='')
        roundlist.append((player+1,[cards]))
        input()
    print(f"Round{round}")
    input()
    finallist.append(roundlist)

print(finallist)

class Game:
    def __init__(self,numplayers,numrounds) -> None:
        self.numplayers = numplayers
        self.numrounds = numrounds

    def playGame():
        pass