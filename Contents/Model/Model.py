# Model
database = []

class Model:
    
    def __init__(self):
        self.database = database

    def get_data(self):
        return database

    def add_data(self, data):
        self.database.append(data)
    
    def remove_data(self):
        self.database.pop()