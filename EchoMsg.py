"""Q2. Echo Message: How can you create an endpoint in FastAPI 
that takes a message as a query parameter and returns the same message?
"""

from fastapi import FastAPI
from typing import Optional

app= FastAPI()

@app.get("/echo/")
def echoMsg(Message: Optional[str] = None):
    if Message:
        return {"Msg": Message}
    
    return{"Msg": "No Msg Provided"}

#we are changing the port since our HelloWorld Hit takes up port 8000

if __name__ == "__EchoMsg__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8001)

"""
Use this cmd to run on termical to resolve [WinError 10013]
uvicorn EchoMsg:app --reload --host 127.0.0.1 --port 8001
   
"""