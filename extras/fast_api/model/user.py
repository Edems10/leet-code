from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class UserName(BaseModel):
    title: Optional[str] = None
    first: str
    last: str

class User(BaseModel):
    name: UserName
    email: EmailStr
    picture: str

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, orm_user):
        return cls(
            name=UserName(
                title=orm_user.title,
                first=orm_user.first_name,
                last=orm_user.last_name
            ),
            email=orm_user.email,
            picture=orm_user.picture
        )



Base = declarative_base()

class UserORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    picture = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"