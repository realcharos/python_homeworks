import json
import csv
import os

# Employee Class
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

# Employee Manager Class
class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee():
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            print("Employee Records:")
            print(file.read())

    @staticmethod
    def search_employee():
        emp_id = input("Enter Employee ID to search: ")
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:", line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def delete_employee():
        emp_id = input("Enter Employee ID to delete: ")
        lines = []
        found = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            lines = file.readlines()
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    file.write(line)
                else:
                    found = True
        print("Employee deleted successfully!" if found else "Employee not found.")

    @staticmethod
    def menu():
        while True:
            print("\n1. Add Employee\n2. View Employees\n3. Search Employee\n4. Delete Employee\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                EmployeeManager.search_employee()
            elif choice == "4":
                EmployeeManager.delete_employee()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# To-Do Task Class
class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

# To-Do Manager Class
class ToDoManager:
    FILE_NAME = "tasks.json"

    @staticmethod
    def load_tasks():
        if os.path.exists(ToDoManager.FILE_NAME):
            with open(ToDoManager.FILE_NAME, "r") as file:
                return json.load(file)
        return []

    @staticmethod
    def save_tasks(tasks):
        with open(ToDoManager.FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

    @staticmethod
    def add_task():
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        tasks = ToDoManager.load_tasks()
        tasks.append({"task_id": task_id, "title": title, "description": description, "due_date": due_date, "status": status})
        ToDoManager.save_tasks(tasks)
        print("Task added successfully!")

    @staticmethod
    def view_tasks():
        tasks = ToDoManager.load_tasks()
        if not tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in tasks:
            print(f"{task['task_id']}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")

    @staticmethod
    def menu():
        while True:
            print("\n1. Add Task\n2. View Tasks\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                ToDoManager.add_task()
            elif choice == "2":
                ToDoManager.view_tasks()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# Run the Programs
if __name__ == "__main__":
    print("Welcome!\n1. Employee Manager\n2. To-Do Manager\n3. Exit")
    app_choice = input("Enter your choice: ")
    if app_choice == "1":
        EmployeeManager.menu()
    elif app_choice == "2":
        ToDoManager.menu()
    else:
        print("Goodbye!")