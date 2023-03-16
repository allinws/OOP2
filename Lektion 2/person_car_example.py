from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Import SQLAlchemy's base class to be inherited from all python classes
Base = declarative_base()

# Define which DB to use, and if to log queries to terminal
# engine = create_engine('sqlite:///mydb.db', echo=False)
engine = create_engine('sqlite:///person_car.db', echo=True)

class Person(Base):
    __tablename__ = 'people'

    personal_number = Column('personal_number', String(11), primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    age = Column('age', Integer)

    def __init__(self, personal_number, first_name, last_name, age):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.personal_number} - {self.first_name} {self.last_name}'
    

class Car(Base):
    __tablename__ = 'cars'

    id = Column('car_id', Integer, primary_key=True)
    owner = Column(String, ForeignKey('people.personal_number'))
    brand = Column('brand', String)
    model = Column('model', String)

    def __init__(self, id, owner, brand, model):
        self.id = id
        self.owner = owner
        self.brand = brand
        self.model = model

    def __repr__(self) -> str:
        return f'({self.id}) {self.brand} {self.model}'
    
# Create all classes above in Db
Base.metadata.create_all(bind=engine)


person_one = Person(
    personal_number='900806-2020', 
    first_name='Alexander', 
    last_name='Lindgren', 
    age=32
)

person_two = Person(
    personal_number='890506-2312',
    first_name='Johan',
    last_name= 'Löfving', 
    age=35
)

person_three = Person(
    personal_number='880506-2312', 
    first_name='Emma', 
    last_name='Olsson', 
    age=33
)

people_to_add = [
    person_one,
    person_two,
    person_three
]

# Session used to communicate with DB
Session = sessionmaker(bind=engine)
session = Session()


for person in people_to_add:
    existing_person = session.query(Person).filter_by(personal_number=person.personal_number).first()
    if existing_person is None:
        session.add(person)

car_one = Car(
    id=1, 
    owner=person_one.personal_number, 
    brand='BMW', 
    model='M3'
)

car_two = Car(
    id=2, 
    owner=person_one.personal_number, 
    brand='Audi', 
    model='RS4'
)

car_three = Car(
    id=3, 
    owner=person_two.personal_number, 
    brand='Saab', 
    model='93'
)

cars = [car_one, car_two, car_three]

for car in cars:
    existing_car = session.query(Car).filter_by(id=car.id).first()
    if existing_car is None:
        session.add(car)

session.commit()


# Query 1: Ger people with specific names
first_names = ['Alexander', 'Johan']
results = session.query(Person).filter(Person.first_name.in_(first_names)).all()
print('\n QUERY 1: PEOPLE MATCHING NAMES')
print(results)
print('\n')


# QUERY 2: Get all cars and their owners' full names:
cars = session.query(Car, Person).join(Person, Car.owner == Person.personal_number).all()
print('\n QUERY 2: ALL CARS AND OWNERS FULL NAMES')
for car, person in cars:
    print(f'{car} - {person.first_name} {person.last_name}')
print('\n')

# QUERY 3: Get all cars owned by a specific person
person_name = 'Alexander Lindgren'
cars = session.query(Car).join(Person, Car.owner == Person.personal_number).filter(Person.first_name + ' ' + Person.last_name == person_name).all()
print('\n QUERY 3: ALL CARS OWNED BY A SPECIFIC PERSON')
print(cars)
print('\n')

# QUUERY 4: Get number of cars owned by each person
from sqlalchemy import func
car_counts = session.query(Person.first_name, Person.last_name, func.count(Car.id)).join(Car).group_by(Person.personal_number).all()
print('\n QUERY 4: NUMBER OF CARS OWNED BY EACH PERSON')
for first_name, last_name, count in car_counts:
    print(f'{first_name} {last_name} - {count}')
print('\n')


# QUERY 5: Update a persons age
person_to_update = session.query(Person).filter_by(personal_number='900806-2020').first()
print('\n QUERY 5: PERSON AGE BEFORE UPDATE')
print(person_to_update.age)
person_to_update.age = 33
session.commit()
print('\n QUERY 5: PERSON AGE UPDATED')
print(person_to_update.age)
print('\n')