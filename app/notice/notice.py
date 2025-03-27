# from fastapi import FastAPI, Path, Query
# from pydantic import  BaseModel, Field, validator
#
# app = FastAPI()
#
# class Item(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50)
#     price: float = Field(..., gt=0, lt=1000000)
#     in_stock: bool = Field(default=True)
#
#         @validator("name")
#             def validate_name(cls, value):
#                 if "@" in value:
#                     raise ValueError("Имя не должно содержать '@'")
#                 return value
#
# items = {
#     1: {"name": "phone", "price": 200},
#     2: {"name": "laptop", "price": 300},
#     3: {"name": "clock", "price": 100},
# }


#
#
# @app.get("/items/{item_id}")
# def get_item(
#         item_id: int = Path(..., gt=0),
#         name: str = Query(None, min_length=3, max_length=50)):
#     return {"item_id": item_id, "name": name}
#
# @app.post("/items/")
# def create_item(item: Item):
#     return {"message": "product is created", "item": item}

# @app.get("/items/")
# def get_items(db: Session = Depends(get_db)):
#     items = db.query(Item).all()
#     return items
#
# @app.post("/items/", response_model=ItemResponse)
# def create_item(item: ItemCreate, db: Session = Depends(get_db)):
#     db_item = Item(**item.model_dump())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item