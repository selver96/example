from sqlalchemy import Column, Integer, String

from .database import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    surname = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
    }