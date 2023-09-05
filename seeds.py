from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review  # Import Base from models

# Create a SQLite database
engine = create_engine('sqlite:///migrations_test.db')

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=2)
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")

# Add sample data to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])

# Commit the changes to the database
session.commit()
