from fastapi import FastAPI, Depends, HTTPException
from scripts.regsetup import description
from routes.auth import router as auth_router
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from exceptions import ItemNotFoundError, DuplicateItemError
import models, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Items

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    # existing_item = db.query(models.Item).filter(models.Item.name == item.name).first()
    # if existing_item:
    #     raise  DuplicateItemError()
    category = db.query(models.Category).filter(models.Category.id == item.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # new_item = models.Item(**item.model_dump())
    new_item = models.Item(name=item.name, description=item.description, category_id=item.category_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get('/items/{item_id}', response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise ItemNotFoundError()
    return item

@app.put("/items/{item_id}", response_model=schemas.ItemUpdate)
def update_item(item_id: int, item: schemas.ItemUpdate, db:Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise ItemNotFoundError()
        # raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.model_dump(exclude_unset=True).items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item  = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise ItemNotFoundError()
        # raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

# Category

@app.post("/categories/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == item.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")

    new_item = models.Item(name=item.name, description=item.description, category_id=item.category_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

