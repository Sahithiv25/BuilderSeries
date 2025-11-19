from fastapi import FastAPI #import
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float
    in_stock:bool = True


app = FastAPI() # instantiate app

@app.get("/")
def read_root():
    return {"message": "Hello user, FastAPI is running."} # Test this in browser

@app.post("/items")
def create_item(item:Item):
    return {
        "message": "Item created successfully",
        "item": item
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search")
def search_items(q: str = None):
    return {"query": q}

items_db = []

@app.post("/add")  # add items = post
def add_item(item: Item):
    items_db.append(item)
    return {"status": "added", "total_items": len(items_db)}

@app.get("/all") # fetch items = get
def read_all_items():
    return items_db