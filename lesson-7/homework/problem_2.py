import json
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary,
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["employee_id"], data["name"], data["position"], data["salary"])

class EmployeeManager:
    FILE_PATH = "employees.json"

    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                return [Employee.from_dict(emp) for emp in json.load(file)]
        return []

    def save_employees(self):
        with open(self.FILE_PATH, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)

    def add_employee(self, employee):
        if any(emp.employee_id == employee.employee_id for emp in self.employees):
            print("Employee ID must be unique!")
            return
        self.employees.append(employee)
        self.save_employees()
        print("Employee added successfully!")

    def view_employees(self):
        for emp in self.employees:
            print(emp.to_dict())

    def search_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                print(emp.to_dict())
                return emp
        print("Employee not found!")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                if name:
                    emp.name = name
                if position:
                    emp.position = position
                if salary:
                    emp.salary = salary
                self.save_employees()
                print("Employee updated successfully!")
                return
        print("Employee not found!")

    def delete_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        self.save_employees()
        print("Employee deleted successfully!")


class ToDoManager:
    FILE_PATH = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.FILE_PATH, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_id, title, description, due_date, status):
        if any(task["task_id"] == task_id for task in self.tasks):
            print("Task ID must be unique!")
            return
        self.tasks.append({"task_id": task_id, "title": title, "description": description, "due_date": due_date, "status": status})
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task["task_id"] == task_id:
                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                if due_date:
                    task["due_date"] = due_date
                if status:
                    task["status"] = status
                self.save_tasks()
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["task_id"] != task_id]
        self.save_tasks()
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task["status"] == status]
        for task in filtered_tasks:
            print(task)


def main():
    emp_manager = EmployeeManager()
    todo_manager = ToDoManager()

    while True:
        print("""
        1. Add Employee
        2. View Employees
        3. Search Employee
        4. Update Employee
        5. Delete Employee
        6. Add Task
        7. View Tasks
        8. Update Task
        9. Delete Task
        10. Filter Tasks
        11. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_manager.add_employee(Employee(input("ID: "), input("Name: "), input("Position: "), input("Salary: ")))
        elif choice == "2":
            emp_manager.view_employees()
        elif choice == "3":
            emp_manager.search_employee(input("Enter Employee ID: "))
        elif choice == "4":
            emp_manager.update_employee(input("ID: "), input("New Name: "), input("New Position: "), input("New Salary: "))
        elif choice == "5":
            emp_manager.delete_employee(input("ID: "))
        elif choice == "6":
            todo_manager.add_task(input("Task ID: "), input("Title: "), input("Description: "), input("Due Date: "), input("Status: "))
        elif choice == "7":
            todo_manager.view_tasks()
        elif choice == "8":
            todo_manager.update_task(input("Task ID: "), input("New Title: "), input("New Description: "), input("New Due Date: "), input("New Status: "))
        elif choice == "9":
            todo_manager.delete_task(input("Task ID: "))
        elif choice == "10":
            todo_manager.filter_tasks(input("Status: "))
        elif choice == "11":
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
