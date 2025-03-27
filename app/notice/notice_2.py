# class Item(BaseModel):
#     name: str

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
#
# @app.get("/items/{item_id}")
# def get_items(item_id: int):
#     if item_id in items:
#         return {"item": items[item_id]}
#     return {"error": "product not found"}

# @app.post("/items/")
# def create_item(item: Item):
#     item_id = len(items) + 1
#     items[item_id] = item.dict()
#     return {"message": f"product is created", "item_id": item_id, "item": items[item_id]}


#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id in items:
#         items[item_id] = item.dict()
#         return {"message": f"product {item_id} update", "item": items[item_id]}
#     return {"error": "product not found"}

# items = {
#     1: {"name": "phone"},
#     2: {"name": "laptop"},
#     3: {"name": "clock"},
# }
#
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     if item_id in items:
#         del items[item_id]
#         return {"message": f"product {item_id} deleted"}
#     return {"error": "product not found"}