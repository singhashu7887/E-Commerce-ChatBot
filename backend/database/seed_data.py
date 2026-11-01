# backend/database/seed_data.py

"""
Seed the database with dummy users for testing.
Run this once: python -m backend.database.seed_data
"""

import bcrypt
from database.db_manager import db

DUMMY_USERS = [
    {
        "user_id": "U001",
        "name": "Ashutosh Singh",
        "email": "Ashutosh@example.com",
        "password": "demo123"
    },
    {
        "user_id": "U002",
        "name": "Test User",
        "email": "test@example.com",
        "password": "test123"
    },
    {
        "user_id": "U003",
        "name": "Sneha Reddy",
        "email": "sneha.reddy@workmail.com",
        "password": "sneha123"
    },
    {
        "user_id": "U004",
        "name": "Rohan Sharma",
        "email": "rohan.s@gmail.com",
        "password": "rohan123"
    }
]


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def seed_users():
    """Create dummy users in the database."""
    print("🌱 Seeding dummy users...")
    
    for user in DUMMY_USERS:
        password_hash = hash_password(user["password"])
        success = db.create_user(
            user_id=user["user_id"],
            name=user["name"],
            email=user["email"],
            password_hash=password_hash
        )
        
        if success:
            print(f"✅ Created user: {user['name']} ({user['email']}) - Password: {user['password']}")
        else:
            print(f"⚠️  User already exists: {user['email']}")
    
    print("\n✨ Seeding complete!")
    print("\n🔑 Login Credentials:")
    for user in DUMMY_USERS:
        print(f"   Email: {user['email']} | Password: {user['password']}")


if __name__ == "__main__":
    seed_users()