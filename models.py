from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, desc
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the association table for reviews
reviews_association = Table(
    'reviews_association',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
   
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews_association', backref='restaurant', overlaps="restaurant")

    def all_reviews(self):
        # Get all reviews for this restaurant as a list of strings
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars." for review in self.reviews]
    
    def __str__(self):
        return self.name 
        
    @classmethod
    def fanciest(cls):
        # Find the restaurant with the highest price
        return session.query(Restaurant).order_by(desc(Restaurant.price)).first()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary="reviews_association", back_populates='customers',overlaps="restaurant")

    def full_name(self):
        # Return the full name of the customer
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Find the restaurant with the highest star rating reviewed by this customer
        return session.query(Restaurant).join(Review).filter(Review.customer_id == self.id).order_by(desc(Review.star_rating)).first()

    def add_review(self, restaurant, rating):
        # Create a new review for the restaurant with the given rating
        review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        # Delete all reviews by this customer for a given restaurant
        reviews_to_delete = session.query(Review).filter_by(customer=self, restaurant=restaurant).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

# Create an engine and session
engine = create_engine('sqlite:///migrations_test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create and add restaurants
restaurant1 = Restaurant(name="Altonas", price=3)
restaurant2 = Restaurant(name="Meat Lovers", price=4)
restaurant3 = Restaurant(name="Leviticus", price=5)

session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()

# Create and add customers
customer1 = Customer(first_name="Ngugi", last_name="Wa Thiong'o")
customer2 = Customer(first_name="Margaret", last_name="Ogola")
customer3 = Customer(first_name="Chinua", last_name="Achebe")

session.add_all([customer1, customer2, customer3])
session.commit()

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)
customer2.add_review(restaurant3, 4)
customer3.add_review(restaurant2, 5)
customer3.add_review(restaurant3, 5)

# Test methods
print("All Reviews for Restaurant One:")   #All Reviews for Restaurant One:
for review in restaurant1.all_reviews():   # Review for Altonas by Ngugi Wa Thiong'o: 4 stars.
    print(review)                          #Review for Altonas by Margaret Ogola: 3 stars.

print("\nFanciest Restaurant:")            #Fanciest Restaurant:
fanciest = Restaurant.fanciest()           #Restaurant Three - Price: 5
print(f"{fanciest.name} - Price: {fanciest.price}")

print("\nFull Name of Customer 1:")        #Full Name of Customer 1:
print(customer1.full_name())               #Ngugi Wa Thiong'o

print("\nFavorite Restaurant for Customer 2:")  #Favorite Restaurant for Customer 2:
favorite = customer2.favorite_restaurant()      #Leviticus - Star Rating: 4
print(f"{favorite.name} - Star Rating: {favorite.reviews[0].star_rating}")

print("\nDeleting All Reviews for Restaurant Three by Customer 3:")   
customer3.delete_reviews(restaurant3)

print("\nAll Reviews for Restaurant Three after Deletion:")  #All Reviews for Restaurant Three after Deletion:
for review in restaurant3.all_reviews():                     #Review for Leviticus by Margaret Ogola: 4 stars.
    print(review)
