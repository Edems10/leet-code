from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
from model.user import User, UserORM, UserName

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: str, db: Session = Depends(get_db)):
    db_user = UserORM(
        title=user.name.title,
        first_name=user.name.first,
        last_name=user.name.last,
        email=user.email,
        picture=user.picture,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User(
        id=db_user.id,
        name=UserName(
            title=db_user.title, first=db_user.first_name, last=db_user.last_name
        ),
        email=db_user.email,
        picture=db_user.picture,
    )


@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(UserORM).offset(skip).limit(limit).all()
    return [
        User(
            id=user.id,
            name=UserName(title=user.title, first=user.first_name, last=user.last_name),
            email=user.email,
            picture=user.picture,
        )
        for user in users
    ]


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserORM).filter(UserORM.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(
        id=db_user.id,
        name=UserName(
            title=db_user.title, first=db_user.first_name, last=db_user.last_name
        ),
        email=db_user.email,
        picture=db_user.picture,
    )
