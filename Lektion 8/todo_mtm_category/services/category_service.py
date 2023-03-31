from models.models import Category, db

class CategoryService:
    
    def create(self, name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
    
    def update(self, category_id, name):
        category = Category.query.get(category_id)
        if category:
            category.name = name
            db.session.commit()
            return category
        return None
    
    def delete(self, category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return f"Category with id {category_id} has been deleted."
        return None
    
    def get_all(self):
        return Category.query.all()