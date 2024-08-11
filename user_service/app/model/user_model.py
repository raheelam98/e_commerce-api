from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional

class UserBase(SQLModel):
    user_name: str
    address: str
    phone_number: int

class UserAuth(SQLModel):
    user_email: str
    user_password: str   

class UserModel(UserBase, UserAuth):
    pass     

class User(UserModel, table=True):
    user_id : Optional[int] =  Field(default=None, primary_key=True) 

class UserUpdateModel(SQLModel):
    user_name: str | None
    address: str | None
    phone_number: str | None
    user_password: str | None   



