from fastapi import FastAPI
app = FastAPI()

#acesso: http://127.0.0.1:8000
@app.get("/helloword")
async def root():
    return {"message": "Hello World !!"}

#acesso: http://127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": "deu certo"}