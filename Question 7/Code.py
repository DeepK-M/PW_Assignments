# Hotel Management System using OOPs

class Room:
    def __init__(self, room_number, room_type, rate):
        self.__room_number = room_number   # Encapsulated (Private)
        self.room_type = room_type
        self.rate = rate
        self.available = True
        self.guest_name = None

    # Getter for private attribute
    def get_room_number(self):
        return self.__room_number

    # Method to book a room
    def book_room(self, guest_name):
        if self.available:
            self.available = False
            self.guest_name = guest_name
            print(f"Room {self.__room_number} booked successfully for {guest_name}.")
        else:
            print(f"Room {self.__room_number} is already booked.")

    # Method to check-in a guest
    def check_in(self, guest_name):
        if not self.available and self.guest_name == guest_name:
            print(f"{guest_name} has checked into Room {self.__room_number}.")
        else:
            print(f"Check-in failed for {guest_name}.")

    # Method to check-out a guest
    def check_out(self):
        if not self.available:
            print(f"{self.guest_name} has checked out from Room {self.__room_number}.")
            self.available = True
            self.guest_name = None
        else:
            print(f"Room {self.__room_number} is already vacant.")


# Inherited class for Suite Room
class SuiteRoom(Room):
    def __init__(self, room_number, rate, has_jacuzzi=True):
        super().__init__(room_number, "Suite", rate)
        self.has_jacuzzi = has_jacuzzi

    def suite_details(self):
        jacuzzi_info = "with Jacuzzi" if self.has_jacuzzi else "without Jacuzzi"
        print(f"Suite Room {self.get_room_number()} ({jacuzzi_info}) at rate {self.rate}.")


# Inherited class for Standard Room
class StandardRoom(Room):
    def __init__(self, room_number, rate, free_breakfast=True):
        super().__init__(room_number, "Standard", rate)
        self.free_breakfast = free_breakfast

    def standard_details(self):
        breakfast_info = "with Free Breakfast" if self.free_breakfast else "without Free Breakfast"
        print(f"Standard Room {self.get_room_number()} ({breakfast_info}) at rate {self.rate}.")


# --------- Example Usage ---------
if __name__ == "__main__":
    # Creating rooms
    suite1 = SuiteRoom(101, 5000)
    standard1 = StandardRoom(201, 2000)

    # Room details
    suite1.suite_details()
    standard1.standard_details()

    # Booking, check-in, check-out
    suite1.book_room("Alina")
    suite1.check_in("Amita")
    suite1.check_out()

    standard1.book_room("Balaji")
    standard1.check_in("Balaji")
    standard1.check_out()




#Sample Output:
# Standard Room 201 (with Free Breakfast) at rate 2000.
# Room 101 booked successfully for Alina.
# Check-in failed for Amita.
# Alina has checked out from Room 101.
# Room 201 booked successfully for Balaji.
# Balaji has checked into Room 201.
# Balaji has checked out from Room 201.