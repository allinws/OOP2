import models

class UserService:
    
    def __init__(self):
        self.model = models.UserModel()

    def create(self, name, email):
        return self.model.create(name, email)
    
    def update(self, user_id, name, email):
        return self.model.update(user_id, name, email)
    
    def delete(self, user_id):
        return self.model.delete(user_id)