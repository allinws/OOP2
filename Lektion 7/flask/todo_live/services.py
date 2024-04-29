import models

class UserService:
    
    def __init__(self):
        self.model = models.UserModel()

    def create(self, name, email):
        # Annan "affärslogik" kan integreras här
        # Här kan vi skicka ett mail till användaren
        # osv.
        return self.model.create(name, email)