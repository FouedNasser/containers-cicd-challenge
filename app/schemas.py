from pydantic import BaseModel, EmailStr

# Schema for creating a user (Input)
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema for returning user data (Output) - NO PASSWORD HERE
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# Schema for JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str
