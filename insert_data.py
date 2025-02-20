from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Order, Restaurant

def insert_data():
    session = SessionLocal()

    try:
        user1 = User(name="Alice Johnson", email="alice@example.com", age=28)
        user2 = User(name="Bob Smith", email="bob@example.com", age=35)
        session.add_all([user1, user2])
        session.commit() 

        print(f"Inserted Users: {user1.id} - {user1.name}, {user2.id} - {user2.name}")

        restaurant1 = Restaurant(name="Pizza Palace", location="Downtown")
        restaurant2 = Restaurant(name="Sushi World", location="Uptown")
        session.add_all([restaurant1, restaurant2])
        session.commit()  # Commit restaurants

        print(f"Inserted Restaurants: {restaurant1.id} - {restaurant1.name}, {restaurant2.id} - {restaurant2.name}")

        order1 = Order(description="Large Pepperoni Pizza", user_id=user1.id, restaurant_id=restaurant1.id)
        order2 = Order(description="California Roll", user_id=user2.id, restaurant_id=restaurant2.id)
        session.add_all([order1, order2])
        session.commit() 

        print(f"Inserted Orders: {order1.id} - {order1.description}, {order2.id} - {order2.description}")

    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback() 
    finally:
        session.close()  

if __name__ == "__main__":
    insert_data()
