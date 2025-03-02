from typing import List
from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import sessionmaker
from base import Database
from model.user import User

class SQLiteDatabase(Database):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def insert_user(self, user:User)->bool:
        with self.Session() as session:
            try:
                session.add(user)
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                print(f"Error inserting user: {e}")
                return False

    def list_all_users(self) -> List[User]:
        with self.Session() as session:
            try:
                orm_users = session.query(UserORM).all()
                return [User.from_orm(user) for user in orm_users]
            except Exception as e:
                print(f"Error listing users: {e}")
                return []
