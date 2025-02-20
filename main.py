from database import SessionLocal, engine, Base
from models import User, Order, Restaurant
from crud import create_user, get_users

# Create all tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Create a new user if needed
new_user = create_user(db, "Aashish Yadav", "Aashish@example.com", 21)
print("User created successfully.")

db.close()
