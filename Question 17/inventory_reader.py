import os

def read_inventory():
    # Get the folder where this script is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(base_path, "inventory.txt")
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("Contents of inventory.txt:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error while reading file: {str(e)}")


if __name__ == "__main__":
    read_inventory()
