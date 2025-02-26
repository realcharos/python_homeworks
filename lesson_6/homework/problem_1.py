def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.read()
            print(records if records else "No records found.")
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        choice = input("1. Add Employee\n2. View Employees\n3. Exit\nChoice: ")
        if choice == "1": add_employee()
        elif choice == "2": view_employees()
        elif choice == "3": break
        else: print("Invalid choice, try again.")

main()