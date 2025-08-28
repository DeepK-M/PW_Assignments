class Student:
    def __init__(self, name, age, roll_number):
        # Encapsulated attributes (private with __ )
        self.__name = name
        self.__age = age
        self.__roll_number = roll_number

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_roll_number(self):
        return self.__roll_number

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:   # Validation
            self.__age = age
        else:
            print("Age must be positive!")

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    # Method to display student details
    def display_info(self):
        print("----- Student Information -----")
        print(f"Name        : {self.__name}")
        print(f"Age         : {self.__age}")
        print(f"Roll Number : {self.__roll_number}")
        print("-------------------------------")

    # Method to update student details
    def update_details(self, name=None, age=None, roll_number=None):
        if name is not None:
            self.set_name(name)
        if age is not None:
            self.set_age(age)
        if roll_number is not None:
            self.set_roll_number(roll_number)


# ------------------ Testing the Class ------------------

# Create student objects
student1 = Student("Alisha", 20, "A-371001")
student2 = Student("Bina", 21, "B-372003")

# Display info
student1.display_info()
student2.display_info()

# Update details
student1.update_details(name="Alia", age=21)
print("\nAfter Updating Student 1:")
student1.display_info()

# Using setters directly
student2.set_name("Rohan")
student2.set_age(22)
print("\nAfter Updating Student 2:")
student2.display_info()



#Sample Output:
# ----- Student Information -----
# Name        : Alisha
# Age         : 20
# Roll Number : A-371001
# -------------------------------
# ----- Student Information -----
# Name        : Bina
# Age         : 21
# Roll Number : B-372003
# -------------------------------

# After Updating Student 1:
# ----- Student Information -----
# Name        : Alia
# Age         : 21
# Roll Number : A-371001
# -------------------------------

# After Updating Student 2:
# ----- Student Information -----
# Name        : Rohan
# Age         : 22
# Roll Number : B-372003
# -------------------------------