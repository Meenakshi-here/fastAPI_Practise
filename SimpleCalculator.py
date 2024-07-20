"""Simple Calculator: How do you create an endpoint that performs 
basic arithmetic operations (addition, subtraction, multiplication, division)?"""

from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/calculate/")
def calculate(operation:str, num1: float, num2: float):
    if operation == "add":
        result = num1 +num2

    elif operation == "subtract":
        result = num1-num2

    elif operation == "multiply":
        result = num1*num2

    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail ="denominator cannot be 0")
        result = num1/num2

    else:
        raise HTTPException(status_code=400, detail= "Invalid Operation given")
    

    return{"operation": operation, "num1":num1, "num2":num2, "result":result}


"""
Your Url would be : http://127.0.0.1:8000/calculate/?operation=add/sub/multi/div &num1=20&num2=10
"""