from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from dependencies import get_current_user
from securite import get_password_hash, verify_password, create_access_token
import models, schemas

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email уже занят")

    hashed_password = get_password_hash(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)


    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.email).first()

    # if not user or not verify_password(user_data.password, user_data.email):
    #     raise HTTPException(status_code=400, detail="Неверная почта или пароль")

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {"message": "Доступ разрешен!", "user": user}