from fastapi import FastAPI
from random import choice
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewName(BaseModel):
    name: str


names = ['Joãozinho', 'Caralho', 'Jack Nicolson', 'Raluca']


@app.get("/name")
def get_name():    
    return { 'name': choice(names) }

@app.post("/name")
def post_name(new_name: NewName):
    message: str

    if new_name.name in names:
        message = 'Já tem lá o burrão'
    else:
        names.append(new_name.name)
        message = 'Adicionado com sucesso'

    return { 'message': message }

