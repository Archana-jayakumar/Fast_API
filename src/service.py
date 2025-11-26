from ast import Delete
from turtle import update
from unittest import result

from .model import Employee, Gender_Employee
from .database import employees_collections
from bson import ObjectId

class EmployeeService:
    async def add_employee(employee_data: dict):
        result = await employees_collections.insert_one(employee_data)
        emp = await employees_collections.find_one({"_id" : result.inserted_id})
        return emp

    async def get_employee(emp_id: int):
        
        if emp_id:
            emp = await employees_collections.find_one({"employee_ID":emp_id}) 
            return emp
        else:
            male = []
            female = []
            emp = await employees_collections.find().to_list()

            for employee in emp:
                if employee.get("gender") == "male":
                    male.append(Employee (** employee))
                else:
                    female.append(Employee (** employee)) #need to convert dict -> pydantic            
                    print(f"emp:{employee.get('gender')}")
                
                    
        return Gender_Employee(male=male,female=female)
        
    async def update(emp_id: int, update_data: dict):
        await employees_collections.update_one({"employee_ID":emp_id},{"$set":update_data}
        )
        emp = await employees_collections.find_one({"employee_ID":emp_id})
        if not emp:
            return None
        return emp
        
    async def delete(emp_id: str):
        result = await employees_collections.delete_one({"employee_ID":emp_id})
        return result.deleted_count > 0

