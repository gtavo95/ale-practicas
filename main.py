from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/bye")
def bye_root():
    return {"Bye": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, dia: str | None = None, q: str | None = None):

    print(f"{item_id=}")
    print(f"{dia=}")
    print(f"{q=}")

    return {
        "result": f"hoy es {dia}, tengo {item_id} nuevos juguetes",
        "documento": {"hijo1": "1", "hijo2": [1, 2, 3, 3], "hijo3": 0, "hijo4": "hola"},
    }

    # return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def uptade_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# schema
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
    currency: str = "GTQ"


@app.post("/items/{item_id}")
def post_item(id: int, item: Item):

    print("------")
    print("printing items:")
    print(item.name)
    print(item.price)
    print(item.is_offer)

    if item.is_offer:
        item.price = item.price * 0.8

    return {"item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# get - traer (queries)
# post - escribir
# put - editar
# delete - borrar

# CRUD operations
# create, read, update and delete
# post, get, put, delete


# https://chat.baalam.ai/app/message
# query param
# ?code=Q4AG1vyRxamgWr2cFC4IFusLlO-3H2gzROq9yd8YDT7&
# state=857afb3d-29cf-4688-a359-ce80fdcb473a&
# iss=https%3A%2F%2Foidc.baalam.ai
# code, state, iss
