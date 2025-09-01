def create_employee_file():
    file_name = "employees.txt"
    
    # Sample employee data
    employees = [
        {"name": "Amit Sharma", "age": 30, "salary": 50000},
        {"name": "Priya Verma", "age": 28, "salary": 60000},
        {"name": "Rajesh Kumar", "age": 35, "salary": 75000},
        {"name": "Sneha Gupta", "age": 25, "salary": 45000}
    ]
    
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Name\t\tAge\tSalary\n")
            file.write("-" * 30 + "\n")
            for emp in employees:
                file.write(f"{emp['name']}\t{emp['age']}\t{emp['salary']}\n")
        print(f"Employee details written successfully to '{file_name}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


# Run the function
if __name__ == "__main__":
    create_employee_file()
