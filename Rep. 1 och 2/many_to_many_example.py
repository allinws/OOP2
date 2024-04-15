from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Step 1: Define the association table as a class model
class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)

# Step 2: Define the tables involved in the relationship
class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rights = relationship("Right", secondary="association", back_populates="lefts")

class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lefts = relationship("Left", secondary="association", back_populates="rights")


def create_db():
    # Create the engine and tables
    engine = create_engine('sqlite:///many_many.sqlite')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example usage
    left1 = Left(name='Left 1')
    right1 = Right(name='Right 1')
    left1.rights.append(right1)

    session.add(left1)
    session.add(right1)
    session.commit()

    # Query example
    left_with_rights = session.query(Left).filter_by(name='Left 1').first()
    print(left_with_rights.rights[0].name)  # Output: 'Right 1'

if __name__ == "__main__":
    create_db()
