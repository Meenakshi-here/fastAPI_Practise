"""Q1. Hello World: How do you create a basic FastAPI application 
that returns "Hello, World!" when accessed?
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def returnMsg():
    return {"msg": "Hello World"}

