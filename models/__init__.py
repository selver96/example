from pydantic import BaseModel

class EmployeeBase(BaseModel):
    id: int
    name: str
    surname: str
    email: str

class EmployeeBody(BaseModel):
    name: str
    surname: str
    email: str