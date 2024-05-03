from ..models import models

class UserService:
    
    def __init__(self):
        self.model = models.UserModel()

    def create(self, name, email, password):
        return self.model.create(name, email, password)
    
    def update(self, user_id, name, email):
        return self.model.update(user_id, name, email)
    
    def delete(self, user_id):
        return self.model.delete(user_id)
    
    def get_all(self):
        return self.model.get_all()
    
    def get_by_email_and_password(self, email, password):
        return self.model.get_by_email_and_password(email, password)