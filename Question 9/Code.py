# Event Management System using OOPs

class Event:
    def __init__(self, event_id, name, date, time, location):
        self.__event_id = event_id         # Encapsulated (Private)
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.__attendees = []              # Encapsulated list of attendees

    # Getter for private attribute
    def get_event_id(self):
        return self.__event_id

    # Create new event
    def create_event(self):
        print(f"Event '{self.name}' (ID: {self.__event_id}) created on {self.date} at {self.time}, Location: {self.location}")

    # Add attendee
    def add_attendee(self, attendee_name):
        self.__attendees.append(attendee_name)
        print(f"{attendee_name} has been added to the event '{self.name}'.")

    # Remove attendee
    def remove_attendee(self, attendee_name):
        if attendee_name in self.__attendees:
            self.__attendees.remove(attendee_name)
            print(f"{attendee_name} has been removed from the event '{self.name}'.")
        else:
            print(f"{attendee_name} is not in the attendee list.")

    # Get total number of attendees
    def get_total_attendees(self):
        return len(self.__attendees)

    # Show attendees
    def show_attendees(self):
        print(f"Attendees for event '{self.name}': {', '.join(self.__attendees) if self.__attendees else 'No attendees yet.'}")


# Inherited class for Private Event
class PrivateEvent(Event):
    def __init__(self, event_id, name, date, time, location, invitation_required=True):
        super().__init__(event_id, name, date, time, location)
        self.invitation_required = invitation_required

    def private_details(self):
        invite_info = "Invitation Required" if self.invitation_required else "No Invitation Required"
        print(f"Private Event '{self.name}' (ID: {self.get_event_id()}) - {invite_info}")


# Inherited class for Public Event
class PublicEvent(Event):
    def __init__(self, event_id, name, date, time, location, max_capacity):
        super().__init__(event_id, name, date, time, location)
        self.max_capacity = max_capacity

    def public_details(self):
        print(f"Public Event '{self.name}' (ID: {self.get_event_id()}) - Max Capacity: {self.max_capacity}")


# --------- Example Usage ---------
if __name__ == "__main__":
    # Creating events
    private_event = PrivateEvent(101, "Birthday Party", "2025-09-10", "07:00 PM", "Hotel Grand", invitation_required=True)
    public_event = PublicEvent(202, "Music Concert", "2025-10-15", "06:00 PM", "City Stadium", max_capacity=5000)

    # Create events
    private_event.create_event()
    public_event.create_event()

    # Add attendees
    private_event.add_attendee("Amit")
    private_event.add_attendee("Bobita")
    public_event.add_attendee("Charan")

    # Show details
    private_event.private_details()
    public_event.public_details()

    # Show attendees
    private_event.show_attendees()
    public_event.show_attendees()

    # Attendee management
    private_event.remove_attendee("Bob")
    private_event.show_attendees()

    # Total count
    print(f"Total attendees in {private_event.name}: {private_event.get_total_attendees()}")
    print(f"Total attendees in {public_event.name}: {public_event.get_total_attendees()}")


# Sample Output:
# Event 'Birthday Party' (ID: 101) created on 2025-09-10 at 07:00 PM, Location: Hotel Grand
# Event 'Music Concert' (ID: 202) created on 2025-10-15 at 06:00 PM, Location: City Stadium
# Amit has been added to the event 'Birthday Party'.
# Bobita has been added to the event 'Birthday Party'.
# Charan has been added to the event 'Music Concert'.
# Private Event 'Birthday Party' (ID: 101) - Invitation Required
# Public Event 'Music Concert' (ID: 202) - Max Capacity: 5000
# Attendees for event 'Birthday Party': Amit, Bobita
# Attendees for event 'Music Concert': Charan
# Bob is not in the attendee list.
# Attendees for event 'Birthday Party': Amit, Bobita
# Total attendees in Birthday Party: 2
# Total attendees in Music Concert: 1