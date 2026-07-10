from fastapi import APIRouter,HTTPException

from app.schemas.user_schema import UserCreate
from app.database.database import users_collection
from app.services.auth_service import hash_password

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
    
)

@router.post("/register")
def register(user:UserCreate):
    
    existing_user = users_collection.find_one(
        {"email":user.email}
    )
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
        
    new_user={
        "full_name":user.full_name,
        "email":user.email,
        "password":hash_password(user.password),
        "role":"user"
    }
    
    users_collection.insert_one(new_user)
    
    return{
        "message":"user registered successfully"
    }

@router.get("/test")
def test_suth():
    return {
        "message":"Authentication Router Working Successfully"
        
    }