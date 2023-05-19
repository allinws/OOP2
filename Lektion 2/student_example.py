from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Import SQLAlchemy's base class to be inherited from all python classes
Base = declarative_base()

# Define which DB to use, and if to log queries to terminal
# engine = create_engine('sqlite:///mydb.db', echo=False)
engine = create_engine('sqlite:///student.db', echo=True)

class Student(Base):
    __tablename__ = 'students'

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
    
# Create all classes above in Db
Base.metadata.create_all(bind=engine)

student_one = Student(
    personal_number='900806-2020', 
    first_name='Alexander', 
    last_name='Lindgren', 
    age=32
)

# Session used to communicate with DB
Session = sessionmaker(bind=engine)
session = Session()

session.add(student_one)

session.commit()