"""Q4. Tp return predefined user profile stored in db
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Define UserProfile class using Pydantic's BaseModel
class UserProfile(BaseModel):
    name: str
    age: int
    designation: str
    email: str

db = UserProfile  (
    name = "Sakthi",
    age = 21,
    designation = "Engineer",
    email= "Sakthi@gmail.com",

)

app = FastAPI()


@app.get("/userprofile/")
def create_user_profile():
    return db