from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Ställer in databasen
engine = create_engine('sqlite:///students.db', echo=False)
Base = declarative_base()

# Definiera Student klassen
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    birthdate = Column(Date)

# Skapa tabeller
Base.metadata.create_all(engine)

# Skapa en session
Session = sessionmaker(bind=engine)
session = Session()

# Skapa tre studenter
student1 = Student(name='Anna Svensson', email='anna.svensson@example.com', birthdate=date(1995, 5, 24))
student2 = Student(name='Karl Andersson', email='karl.andersson@example.com', birthdate=date(1996, 4, 15))
student3 = Student(name='Eva Johansson', email='eva.johansson@example.com', birthdate=date(1997, 2, 3))

print("=== Lägger till Studenter i Databasen ===")
session.add_all([student1, student2, student3])
session.commit()

# Filter queries
print("\n=== Studenter med Namn som Börjar på 'A' ===")
students_a = session.query(Student).filter(Student.name.like('A%')).all()
for student in students_a:
    print(f"Namn: {student.name}, E-post: {student.email}, Födelsedatum: {student.birthdate}")

print("\n=== Student med Specifik E-post ===")
student_email = session.query(Student).filter_by(email='karl.andersson@example.com').first()
if student_email:
    print(f"Namn: {student_email.name}, E-post: {student_email.email}, Födelsedatum: {student_email.birthdate}")

print("\n=== Studenter Födda efter 1996 ===")
students_96 = session.query(Student).filter(Student.birthdate > date(1996, 1, 1)).all()
for student in students_96:
    print(f"Namn: {student.name}, E-post: {student.email}, Födelsedatum: {student.birthdate}")

# Ändra data för en student
print("\n=== Uppdaterar En Students Data ===")
student_to_update = session.query(Student).filter_by(name='Anna Svensson').first()
if student_to_update:
    student_to_update.email = 'updated.anna.svensson@example.com'
    session.commit()

    updated_student = session.query(Student).filter_by(name='Anna Svensson').first()
    print(f"Uppdaterad E-post för {updated_student.name}: {updated_student.email}")
