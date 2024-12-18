from pydantic import BaseModel, Field, EmailStr, ConfigDict  # Pydantic for model validation
from typing import Union, List  # Typing for Union and List types
from fastapi import FastAPI  # FastAPI framework

# Initialize the FastAPI application
app = FastAPI()

# Sample data dictionary (with the "age" key)
data = {
    "email": "abs@mail.uz",  # A valid email address
    "bio": None,             # A bio field set to None
    "age": 12,               # Age of the user
}

# Sample data dictionary (without the "age" key)
data_wo_age = {
    "email": "abs@mail.uz",
    "bio": None,
    # Additional keys are commented out
    # "gender": "Male",
    # "birthday": 2022,
}


# Define the User model
class UserSchema(BaseModel):
    # Email validation using EmailStr type
    email: EmailStr  
    # Bio can be a string or None; maximum length is 10 characters
    bio: Union[str, None] = Field(max_length=10)

    # Disallow additional unexpected keys in the model
    model_config = ConfigDict(extra="forbid")


# A list to store users
users = []

# POST endpoint to create a new user
@app.post("/user")
def create_user(user: UserSchema):
    # Add the new user to the users list
    users.append(user)
    # Return a response indicating success
    return {"ok": True, "msg": "user created"}

# GET endpoint to retrieve all users
@app.get("/users")
def read_users() -> List[UserSchema]:
    # Return the list of users
    return users

# Commented-out code for an extended user model with age validation
# class UserAgeSchema(UserSchema):
#     # Age must be between 0 and 130
#     age: int = Field(ge=0, le=130)

# Tests for the UserSchema model without the "age" key
# print(repr(UserSchema(**data_wo_age)))

# Tests for the UserAgeSchema model
# print(repr(UserAgeSchema(**data)))
