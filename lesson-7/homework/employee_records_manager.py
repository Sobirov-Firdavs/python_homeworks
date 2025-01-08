class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    file_path = r'python_homeworks\lesson-7\homework\employee.txt'

    def __init__(self):
        try:
            with open(self.file_path) as file:
                self.lines = [Employee(*line.strip().split(', ')) for line in file.readlines()]
        except FileNotFoundError:
            self.lines = []

    def add_employee(self):
        employee_id = max(int(emp.employee_id) for emp in self.lines) + 1 if self.lines else 101
        name = input("Enter an employee's name: ")
        position = input("Enter the employee's position: ")
        salary = input("Enter the employee's salary: ")

        new_employee = Employee(str(employee_id), name, position, salary)
        self.lines.append(new_employee)

        with open(self.file_path, 'w') as file:
            file.writelines(f"{emp}\n" for emp in self.lines)
        print("Added successfully!")

    def view_all_records(self):
        if not self.lines:
            print("No employee records found.")
            return
        for emp in self.lines:
            print(f"ID: {emp.employee_id}; Name: {emp.name}; Position: {emp.position}; Salary: {emp.salary}")

    def search_employee(self):
        id_searched = input("Enter an employee's ID: ")
        for emp in self.lines:
            if emp.employee_id == id_searched:
                print(f"ID: {emp.employee_id}; Name: {emp.name}; Position: {emp.position}; Salary: {emp.salary}")
                return
        print("Employee not found.")

    def update_employee(self):
        id_updated = input("Enter an employee's ID: ")
        for emp in self.lines:
            if emp.employee_id == id_updated:
                emp.name = input("Enter a new name (leave blank to keep unchanged): ") or emp.name
                emp.position = input("Enter a new position (leave blank to keep unchanged): ") or emp.position
                emp.salary = input("Enter a new salary (leave blank to keep unchanged): ") or emp.salary
                with open(self.file_path, 'w') as file:
                    file.writelines(f"{emp}\n" for emp in self.lines)
                print("Updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self):
        id_deleted = input("Enter an employee's ID: ")
        new_lines = [emp for emp in self.lines if emp.employee_id != id_deleted]
        if len(new_lines) == len(self.lines):
            print("Employee not found.")
        else:
            self.lines = new_lines
            with open(self.file_path, 'w') as file:
                file.writelines(f"{emp}\n" for emp in self.lines)
            print("Deleted successfully!")

    def menu(self):
        while True:
            print("\nYou have the following options:")
            print("1. Add new employee record.")
            print("2. View all employee records.")
            print("3. Search for an employee by Employee ID.")
            print("4. Update an employee's information.")
            print("5. Delete an employee record.")
            print("6. Exit.")

            option = input("Enter your option: ")
            if option == '1':
                self.add_employee()
            elif option == '2':
                self.view_all_records()
            elif option == '3':
                self.search_employee()
            elif option == '4':
                self.update_employee()
            elif option == '5':
                self.delete_employee()
            elif option == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


# Run the program
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()