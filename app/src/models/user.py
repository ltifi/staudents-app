from pydantic import BaseModel, Field, EmailStr

        
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Sedki Ltifi",
                "email": "sedki.ltifi@gmail.com",
                "password": "yourpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "sedki.ltifi@gmail.com",
                "password": "yourpassword"
            }
        }