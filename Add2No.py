"""Q3. Add Two Numbers: How do you create an endpoint that takes two numbers 
as query parameters and returns their sum?"""

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/add/")
def add_num(Num1: Optional[int] = 10, Num2: Optional[int] = 30):
    return {"Sum": Num1 + Num2}

