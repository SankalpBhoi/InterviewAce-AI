from passlib.context import CryptContext
from fastapi import HTTPException

from app.database.database import users_collection
from app.core.security import create_access_token


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


#Password Verification
def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


#Register user
def register_user(user):
    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = {
        "full_name": user.full_name,
        "email": user.email,
        "password": hash_password(user.password),
        "role": "user"
    }

    users_collection.insert_one(new_user)

    return {
        "message": "User registered successfully"
    }
    
#User Login
def login_user(user):
    # Find the user by email
    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    # Check if user exists
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        user.password,
        existing_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT Token
    access_token = create_access_token(
        {
            "sub": str(existing_user["_id"]),
            "email": existing_user["email"],
            "role": existing_user["role"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }