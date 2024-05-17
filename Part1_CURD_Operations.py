from fastapi import FastAPI

app = FastAPI()

#get method

@app.get("/")
async def root():
    return {"message": "Hello World"}


#post method

@app.post("/items/")
async def create_item(name: str, price: float, description: str = None, tax: float = None):
    item = {"name": name, "price": price}
    if description:
        item.update({"description": description})
    if tax:
        item.update({"tax": tax})
    return item

#put method

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, price: float, description: str = None, tax: float = None):
    item = {"name": name, "price": price}
    if description:
        item.update({"description": description})
    if tax:
        item.update({"tax": tax})
    return {"item_id": item_id, **item}

#delete method

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id}

#patch method

@app.patch("/items/{item_id}")
async def patch_item(item_id: int, name: str = None, price: float = None, description: str = None, tax: float = None):
    item = {"name": name, "price": price}
    if description:
        item.update({"description": description})
    if tax:
        item.update({"tax": tax})
    return {"item_id": item_id, **item}

