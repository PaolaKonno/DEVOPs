#python -m uvicorn main:app --reload
from fastapi import FastAPI
import random
app = FastAPI()

#acesso: http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World !!"}
#acesso: http://127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
modificacao-nomes-endpoints-2
    return{"teste": True, "num_aleatorio": random.randint(0,1000)}

