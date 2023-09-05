# restaurantSQL
Restaurant Review Project
This project is a restaurant review system that allows customers to leave reviews for restaurants and helps them discover the best-rated restaurants. It uses SQLAlchemy for database management and provides a user-friendly interface for interacting with restaurant and customer data.

Table of Contents

Features
Getting Started
Prerequisites
Installation
Usage
Database Schema
Object Relationship Methods
Aggregate and Relationship Methods
Contributing
License

Features

Create and manage restaurants and customer data.
Allow customers to leave reviews for restaurants.
Find the fanciest restaurant based on the highest price.
Get a customer's favorite restaurant based on their reviews.
Delete all reviews by a customer for a specific restaurant.
View all reviews for a particular restaurant.

Getting Started

Prerequisites
Before you begin, ensure you have the following prerequisites installed:

Python (version 3.x)
SQLAlchemy
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/restaurant-review-project.git
Navigate to the project directory:

bash
Copy code
cd restaurant-review-project
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt

Usage

Here's how you can use the Restaurant Review project:

Create instances of restaurants and customers using the provided classes.
Add reviews for restaurants by customers.
Explore various object relationship methods to retrieve information.
Use aggregate and relationship methods to find the fanciest restaurant, get a customer's favorite restaurant, and manage reviews.

Database Schema

The project uses the following database schema:
restaurants table with columns: id, name, price
customers table with columns: id, first_name, last_name
reviews table with columns: id, star_rating, restaurant_id, customer_id
Object Relationship Methods
Review.customer(): Get the Customer instance for a review.
Review.restaurant(): Get the Restaurant instance for a review.
Aggregate and Relationship Methods
Customer.full_name(): Get the full name of a customer.
Customer.favorite_restaurant(): Get the restaurant with the highest star rating from a customer.
Customer.add_review(restaurant, rating): Add a new review for a restaurant.
Customer.delete_reviews(restaurant): Delete all reviews by a customer for a specific restaurant.
Review.full_review(): Get a formatted review string.
Restaurant.fanciest(): Get the restaurant with the highest price.
Restaurant.all_reviews(): Get a list of formatted review strings for all reviews of a restaurant.
Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow the guidelines in CONTRIBUTING.md.

License

This project is licensed under the MIT License - see the LICENSE file for details.
