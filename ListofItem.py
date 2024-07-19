"""Q5. List of Items: 
How do you create an endpoint that returns a list of items?
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Define Item model using Pydantic's BaseModel
class Item(BaseModel):
    name: str
    price: float
    description: str

app = FastAPI()

# Sample list of items
items_db = [
    Item(name="Item1", price=10.99, description="Description of Item1"),
    Item(name="Item2", price=20.99, description="Description of Item2"),
    Item(name="Item3", price=30.99, description="Description of Item3")
]

# Define a GET endpoint to return the list of items
@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db
