from uuid import uuid4
import requests

class Client:
    def __init__(self, name):
        self.name = name
        self.id = uuid4()

    def __str__(self):
        return f'Name:{self.name} \n ID: ({self.id})'
    
    def createSession(self):
        res = requests.post('http://localhost:4160/create/session',json={'Owner':{'id':str(self.id),'name':self.name}})
        return res.text



if  __name__ == '__main__':
    client = Client(input('Enter your username: '))
    print(client)
    print('Connecting to server...')
    id = client.createSession()
    print(id)