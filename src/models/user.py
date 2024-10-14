from database.database import Base
from sqlalchemy import column, Integer, String

class User(Base):                               
    __tablename__ = "users"
    id = column(Integer, primary_key=True, index=True)
    name = column(String)
    email = column(String)
    password = column(String)
    