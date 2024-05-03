from models import User, db

class UserService:
    
    def create(self, name, email, password):
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, user_id, name, email):
        user = User.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
            return user
        return None
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return f"User with id {user_id} has been deleted."
        return None
    
    def get_all(self):
        return User.query.all()
    
    def get_by_email_and_password(self, email, password):
        return User.query.filter_by(email=email, password=password).first()