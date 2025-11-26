from typing import Optional
from fastapi import APIRouter, HTTPException
from .model import AllEmployee, Employee, Gender_Employee, UpdateEmployee
from .service import EmployeeService
from typing import Optional

router = APIRouter()



@router.post("/employees") 
async def create_employee(employee: Employee) -> Employee :
    return await EmployeeService.add_employee(employee.dict())
    

# @router.get("/employees")
# async def get_all_employees():
#     return await EmployeeService.get_all()

@router.get("/employees")
async def get_employee(emp_id: Optional[int] = None) -> Employee | Gender_Employee:
    emp = await EmployeeService.get_employee(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/employees/{emp_id}")
async def update_employee(emp_id: int, employee: UpdateEmployee) -> dict:
    update_data = {k: v for k, v in employee.model_dump().items() if v is not None}
    updated = await EmployeeService.update(emp_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}

@router.delete("/employees/{emp_id}")
async def delete_employee(emp_id: int):
    deleted = await EmployeeService.delete(emp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
