file_path = r'python_homeworks\lesson-6\homework\employees.txt'

def load_employees():
    employees = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Ignore the header line and process valid entries
                if line.strip().startswith('[') and line.strip() != "[['ID', 'Name', 'Position', 'Salary']":
                    line = line.strip('[],\n ')  # Clean brackets, commas, and spaces
                    parts = line.split(',')
                    try:
                        # Extract and convert data
                        emp_id = int(parts[0])
                        name = parts[1].strip().strip("'")
                        position = parts[2].strip().strip("'")
                        salary = int(parts[3].strip().strip("'"))
                        employees.append([emp_id, name, position, salary])
                    except (ValueError, IndexError):
                        print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("File not found. Starting with an empty list of employees.")
    return employees

def save_employees(employees):
    try:
        with open(file_path, 'w') as file:
            file.write("employees = [\n")
            file.write("    ['ID', 'Name', 'Position', 'Salary'],\n")
            for emp in employees:
                file.write(f"    [{emp[0]}, '{emp[1]}', '{emp[2]}', '{emp[3]}'],\n")
            file.write("]")
        print("Changes saved successfully.")
    except IOError:
        print("Error saving to file.")

employees = load_employees()

while True:
    print("""\nYou have the following options:
          1. Add new employee record
          2. View all employee records
          3. Search for an employee by Employee ID
          4. Update an employee's information
          5. Delete an employee record
          6. Exit""")

    try:
        choice = int(input('Enter an option: '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        id1 = employees[-1][0] + 1 if employees else 100
        name = input('Enter his/her name: ')
        job = input('Enter his/her position: ')
        try:
            salary = int(input('Enter his/her salary: '))
            employees.append([id1, name, job, salary])
            print('Employee added.')
        except ValueError:
            print("Invalid salary. Please enter a valid number.")

    elif choice == 2:
        if employees:
            print("ID\tName\t\tPosition\tSalary")
            for emp in employees:
                print(f"{emp[0]}\t{emp[1]}\t{emp[2]}\t{emp[3]}")
        else:
            print('No employees found.')

    elif choice == 3:
        try:
            id3 = int(input("Enter an employee's ID: "))
            employee = next((emp for emp in employees if emp[0] == id3), None)
            if employee:
                print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")
            else:
                print('Employee not found.')
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

    elif choice == 4:
        try:
            id4 = int(input("Enter an employee's ID: "))
            employee = next((emp for emp in employees if emp[0] == id4), None)
            if employee:
                name = input(f"Enter new name (current: {employee[1]}): ") or employee[1]
                job = input(f"Enter new position (current: {employee[2]}): ") or employee[2]
                salary = input(f"Enter new salary (current: {employee[3]}): ")
                salary = int(salary) if salary else employee[3]
                employee[1], employee[2], employee[3] = name, job, salary
                print('Employee updated.')
            else:
                print('Employee not found.')
        except ValueError:
            print("Invalid input. Please try again.")

    elif choice == 5:
        try:
            id5 = int(input("Enter an employee's ID: "))
            employees = [emp for emp in employees if emp[0] != id5]
            print('Employee deleted.')
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

    elif choice == 6:
        save_employees(employees)
        print('Exiting...')
        break

    else:
        print('Invalid option. Please try again.')