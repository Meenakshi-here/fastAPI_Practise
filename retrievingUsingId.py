from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define Item model using Pydantic's BaseModel
class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str

app = FastAPI()


items_db = [
    Item(id=1, name="Item1", price=10.99, description="Description of Item1"),
    Item(id=2, name="Item2", price=20.99, description="Description of Item2"),
    Item(id=3, name="Item3", price=30.99, description="Description of Item3")
]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
