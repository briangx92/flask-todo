from datetime import datetime

class Todos(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.time = datetime.now()

    def complete(self, name):
        name.completed = True
    
    

