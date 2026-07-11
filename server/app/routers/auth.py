from fastapi import APIRouter

from app.schemas.user_schema import UserCreate
from app.services.auth_service import register_user
from app.core.security import create_access_token

from app.schemas.user_schema import UserCreate, UserLogin ,Token
from app.services.auth_service import register_user, login_user

from fastapi import Depends
from app.core.security import get_current_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserCreate):
    return register_user(user)

# @router.post("/login")
# def login(user: UserLogin):
#     return login_user(user)

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    return login_user(user)

@router.get("/test")
def test_auth():
    return {
        "message": "Authentication Router Working Successfully"
    }
    
@router.get("/test-token")
def test_token():
    token = create_access_token(
        {"email": "sankalp@gmail.com"}
    )

    return {
        "access_token": token
    }
    
@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": str(current_user["_id"]),
        "full_name": current_user["full_name"],
        "email": current_user["email"],
        "role": current_user["role"],
    }