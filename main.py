from typing import Annotated

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: Annotated[int, Path(..., title="Item ID", ge=10, le=100)],
        q: str | None = Query(None, min_length=3, max_length=50),
        item: Item | None,
        user: User | None = Body(None)
        ):
    results = {"item_id": item_id, "item": item}

    if q:
        results.update({"q": q})
    if user:
        results.update({"user": user})
    return results