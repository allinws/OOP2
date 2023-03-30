import models

class UserService:
    
    def __init__(self):
        self.model = models.User()

    def create(self, name, email):
        return self.model.create(name, email)