from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    name: str
    gender: str
    project: str
    employee_ID: int
    age: int

class UpdateEmployee(BaseModel):
    name: str | None = None
    gender: str | None = None
    project: str | None = None
    employee_ID: int | None = None
    age: int | None = None

class AllEmployee(BaseModel):
    employees: List[Employee]


class Gender_Employee(BaseModel):
    male : list[Employee]
    female : list[Employee]


