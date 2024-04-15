from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from faker import Faker
import random
import string

Base = declarative_base()


class StudentCourse(Base):
    __tablename__ = "student_course"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)


class Program(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    points = Column(Integer, nullable=True)
    program_id = Column(Integer, ForeignKey("programs.id"))
    students = relationship(
        "Student", secondary="student_course", back_populates="courses"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=True)
    courses = relationship(
        "Course", secondary="student_course", back_populates="students"
    )


def create_database():
    engine = create_engine("sqlite:///school_db5.sqlite")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    program1 = Program(code="abc123", name="abcd")
    session.add(program1)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_database()
