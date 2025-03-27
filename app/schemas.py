from pydantic import BaseModel, EmailStr


# Item

class ItemCreate(BaseModel):
    name: str
    description: str
    category_id: int

class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None



# Category

class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    items: list[ItemResponse] = []

    class Config:
        from_attributes = True


# User

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True