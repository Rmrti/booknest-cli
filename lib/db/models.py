# SQLAlchemy models
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    rentals = relationship("Rental", back_populates="customer", cascade="all, delete")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

    rentals = relationship("Rental", back_populates="book", cascade="all, delete")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', genre='{self.genre}')>"

class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    customer = relationship("Customer", back_populates="rentals")
    book = relationship("Book", back_populates="rentals")

    def __repr__(self):
        return f"<Rental(id={self.id}, customer='{self.customer.name}', book='{self.book.title}')>"

# Database setup
engine = create_engine("sqlite:///lib/db/booknest.db")
Session = sessionmaker(bind=engine)
session = Session()
