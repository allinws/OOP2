from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Skapa en engine som vi kan använda för att skapa en databas
engine = create_engine('sqlite:///pets.db', echo=True)

# Skapa en session som vi kan använda för att interagera med databasen
Session = sessionmaker(bind=engine)
session = Session()

# Skapa en bas som vi kan använda för att definiera våra modeller
Base = declarative_base()

# Definiera våra modeller
class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # Lägg till en relation till Pets
    pets = relationship('Pet', secondary='person_pets', back_populates='owners')

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Lägg till en relation till Persons
    owners = relationship('Person', secondary='person_pets', back_populates='pets')

class PersonPet(Base):
    __tablename__ = 'person_pets'

    person_id = Column(Integer, ForeignKey('persons.id'), primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'), primary_key=True)


# Skapa tabellerna i databasen
Base.metadata.create_all(engine)

# Skapa personer
person1 = Person(name='John Doe')
person2 = Person(name='Jane Smith')

# Skapa husdjur
pet1 = Pet(name='Fluffy')
pet2 = Pet(name='Spot')

# Lägg till husdjuren till personerna
person1.pets.append(pet1)
person1.pets.append(pet2)
person2.pets.append(pet1)

session.add_all([person1, person2, pet1, pet2])

# Commit sessionen för att spara ändringarna till databasen
session.commit()