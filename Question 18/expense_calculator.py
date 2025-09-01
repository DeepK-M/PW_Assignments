import os

def calculate_total_expenses():
    # Get the folder where this script is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(base_path, "expenses.txt")
    
    total = 0
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:  # Expecting "ExpenseName: Amount"
                    try:
                        # Extract the part after ':' and convert to int
                        amount = float(line.split(":")[1].strip())
                        total += amount
                    except ValueError:
                        print(f"Skipping invalid line: {line.strip()}")
        
        print(f"Total Expenses: {total}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error while reading file: {str(e)}")


if __name__ == "__main__":
    calculate_total_expenses()
