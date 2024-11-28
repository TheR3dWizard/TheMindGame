from uuid import uuid4,UUID
from typing import List
from random import choice

class Game:
    def __init__(self,numplayers,numrounds) -> None:
        self.numplayers = numplayers
        self.numrounds = numrounds
        self.cardlist = [i for i in range(1,101)]
        

    def setup(self):
        deals = []

class Player:
    def __init__(self,id:str,name: str):
        self.id = UUID(id)
        self.name = name

    def __eq__(self, id):
        return self.id == id


class Session:
    def __init__(self,players: List[Player] = []):
        self.id = uuid4()
        self.owner = players[0]
        self.players = players
        self.numplayers = len(players)
        self.numrounds = 5
        self.Game = None

    def startGame(self):
        self.Game = Game(self.numplayers,self.numrounds)

    def getId(self):
        return self.id