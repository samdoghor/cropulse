from typing import Union

from fastapi import FastAPI

server = FastAPI()


@server.get("/")
def read_root():
    return {"Hello": "World"}


@server.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
