from typing import List
from db.database import Base, SessionLocal, engine
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from service import employee_srv

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/employee")

TAGS = ["EMPLOYEE"]


@router.post("/create/", response_model=models.EmployeeBase)
def create_employee(employee: models.EmployeeBody, db: Session = Depends(get_db)):
    return employee_srv.create_employee(db=db, employee=employee)



@router.get("/get/", response_model=List[models.EmployeeBase])
def get_employees(db: Session = Depends(get_db)):
    employees = employee_srv.get_employees(db)
    return employees


@router.get("/get/{employee_id}", response_model=models.EmployeeBase)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    db_employee = employee_srv.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_employee