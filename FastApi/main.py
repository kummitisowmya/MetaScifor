from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
mydata = [
    {"id": 1, "name": "sowmya","course":"python","role":"python developer"},
    {"id": 2, "name": "sravani","course":"java","role":"java developer"},
    {"id": 3, "name": "jai","course":"sql","role":"sql developer"},
    {"id": 4, "name": "raghu","course":"frontend","role":"web developer"},
]

class Item(BaseModel):
    name: str

@app.get("/items")
def get_items():
    return mydata

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in mydata:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def create_item(item: Item):
    new_item = {"id": len(mydata) + 1, "name": item.name}
    mydata.append(new_item)
    return {"message": "Item added", "item": new_item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i in range(len(mydata)):
        if mydata[i]["id"] == item_id:
            mydata[i]["name"] = item.name
            return {"message": "Item updated", "item": mydata[i]}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i in range(len(mydata)):
        if mydata[i]["id"] == item_id:
            removed_item = mydata.pop(i)
            return {"message": "Item deleted", "item": removed_item}
    return {"error": "Item not found"}
