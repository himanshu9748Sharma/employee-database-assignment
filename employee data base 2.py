employees = { 1: {"Name": "satya","Age": 24,"Department":"Sales","Salary": 25000},
              2: {"Name": "kiran","Age": 26,"Department":"Sales","Salary": 30000},
              3: {"Name": "prakash","Age": 24,"Department":"HR","Salary": 35000},
              4: {"Name": "aditya","Age": 28,"Department":"Accounts","Salary": 25000},
              5: {"Name": "vikas","Age": 30,"Department":"Accounts","Salary": 35000},
              6: {"Name": "sarvesh","Age": 30,"Department":"Accounts","Salary": 35000},
              7: {"Name": "rohit","Age": 30,"Department":"HR","Salary": 30000},}

# Function to add a new employee
def add_employee():
    """Adds a new employee to data base."""
    print("---- Add new employee ----")
while True:
    try:
     emp_id = int(input("Enter Employee ID: "))
     break
    except ValueError:
         print("invalid input for emp_id. please enter a valid number in integer format.")
    if emp_id in employees:
        print("Employee ID already exists! Please input a new ID.")
        return
    name = input("Enter employee name: ")
while True:
    try:
        age = int(input("Enter employee age: "))
        break
    except ValueError:
        print("invalid input for age. please enter a valid number in integer format.")   
department = input("Enter employee department: ")
while True:
    try:
        salary = int(input("Enter employee salary: "))
        break
    except ValueError:
        print("invalid input for salary. please enter a valid number in integer format.")
employees[emp_id] = {"Name": name, "Age": age, "Department": department, "Salary": salary}
print(f"Employee {name} with ID {emp_id} successfully added.")

# Function to view all employees
def view_employee():
    """Displays details of all employees."""
    print("---- Employee details ----")
    if not employees:
        print("No employees found.")
        return
    print(f"{'ID':<5} {'Name':<10} {'Age':<3} {'Department':<10} {'Salary':<10}")
    print("-" * 50)
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['Name']:<10} {details['Age']:<3} {details['Department']:<10} {details['Salary']:<10}")

# Function to search for an employee by ID
def search_employee():
    """Search for an employee ID and display details."""
    print("---- Search Employee ----")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"Employee found: ID: {emp_id}, Name: {details['Name']}, Age: {details['Age']}, Department: {details['Department']}, Salary: {details['Salary']}")
        else:
            print(f"Employee with ID {emp_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid employee ID.")

if __name__ == "__main__":
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Exit")
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")  