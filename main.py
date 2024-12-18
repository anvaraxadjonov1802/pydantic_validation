from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Union, List
from fastapi import FastAPI

app = FastAPI()


data = {
    "email" : "abs@mail.uz",
    "bio" :  None,
    "age": 12,

}

data_wo_age = {
    "email" : "abs@mail.uz",
    "bio" :  None,
    # "gender" : "Male",
    # "birthday" : 2022,
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: Union[str, None] = Field(max_length=10)

    model_config = ConfigDict(extra="forbid")


users = []

@app.post("/user")
def create_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "user created"}

@app.get("/users")
def read_users() -> List[UserSchema]:
    return users


# class UserAgeSchema(UserSchema):
#     age: int = Field(ge=0, le=130)


# print(repr(UserSchema(**data_wo_age)))
# print(repr(UserAgeSchema(**data)))
