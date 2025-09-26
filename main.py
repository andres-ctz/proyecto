from fastapi import FastAPI
from sqlmodel import SQLModel 

app = FastAPI()

class User(SQLModel): 
    username = str  
    password = str  

user_db = User(username = "andresown", password = "123456")

@app.get("/")
def read_root():
    return {"mensaje":"test login, andres calva"}

class Auto(SQLModel):
    username = str
    password = str

@app.post("/login")
def login(verificar = Auto):
    if verificar == user_db or user_db ==verificar:
        return {"mensaje":"acceso verificado, es correcto"}
    else:
        return{"mensaje":"usuario incorrecto, no vrerificado"}

        #fastapi devfas