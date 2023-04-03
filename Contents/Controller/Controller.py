# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_data(self, data):
        self.model.add_data(data)
    
    def display_data(self):
        self.view.display_data(self.model.get_data())