import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import create_engine, select, Session

from models import *

app = FastAPI(title="Property")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# admin view
engine = create_engine("sqlite:///DB.sqlite")


@app.get("/")
def homepage(request: Request):
    return "HOME"


@app.get("/property/{property_name}")
def search_property_by_name(property_name: str):
    with Session(engine) as session:
        statement = select(Property).where(Property.title == property_name)
        return session.exec(statement).all()


@app.get("/allproperty")
def all_property():
    with Session(engine) as session:
        statement = select(Property)
        return session.exec(statement).all()


@app.get("/user/{user_name}")
def search_user_by_name(user_name: str):
    with Session(engine) as session:
        statement = select(Property).where(Property.title == user_name)
        return session.exec(statement).all()


@app.get("/alluser")
def all_users():
    with Session(engine) as session:
        statement = select(Users)
        return session.exec(statement).all()


@app.post("/register/{text}")
def register_user(text: str, a: str, c: str, d: str):
    with Session(engine) as session:
        statement = select(Property)
    return text


@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,  # port, na ktorom sa aplikácia spustí, default=8000
        host="0.0.0.0",  # bude akceptovať komunikáciu z akejkoľvek IP adresy, default=127.0.0.1
        reload=True,  # v prípade zmeny súboru sa aplikácia automaticky reštartne, default=False
    )
