from sqlalchemy.orm import Session

from db import schemas
from models import EmployeeBase, EmployeeBody

def get_employee(db: Session, employee_id: int) -> EmployeeBase:
    return db.query(schemas.Employee).filter(schemas.Employee.id == employee_id).first().dict()

def get_employees(db: Session) -> EmployeeBase:
    result = []
    employees = db.query(schemas.Employee).all()
    for item in employees:
        result.append(item.dict())
    return result

def create_employee(db: Session, employee: EmployeeBody) -> EmployeeBase:
    db_user = schemas.Employee(name = employee.name, surname = employee.surname, email=employee.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.dict()
