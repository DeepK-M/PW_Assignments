# Airline Reservation System using OOPs

class Flight:
    def __init__(self, flight_id, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats):
        self.__flight_id = flight_id              # Encapsulated (Private)
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.__available_seats = total_seats      # Encapsulated (Private)
        self.booked_passengers = []               # To keep track of passengers

    # Getter for private flight ID
    def get_flight_id(self):
        return self.__flight_id

    # Book a seat
    def book_seat(self, passenger_name):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            self.booked_passengers.append(passenger_name)
            print(f"Seat booked successfully for {passenger_name} on flight {self.flight_number}.")
        else:
            print("No seats available!")

    # Cancel reservation
    def cancel_reservation(self, passenger_name):
        if passenger_name in self.booked_passengers:
            self.booked_passengers.remove(passenger_name)
            self.__available_seats += 1
            print(f"Reservation for {passenger_name} on flight {self.flight_number} has been cancelled.")
        else:
            print(f"No reservation found for {passenger_name}.")

    # Get remaining available seats
    def get_available_seats(self):
        return self.__available_seats

    # Show flight details
    def flight_details(self):
        print(f"Flight {self.flight_number} (ID: {self.__flight_id})")
        print(f"Route: {self.departure_airport} → {self.arrival_airport}")
        print(f"Departure: {self.departure_time}, Arrival: {self.arrival_time}")
        print(f"Available Seats: {self.__available_seats}")
        print("-" * 40)


# Domestic Flight (inherits from Flight)
class DomesticFlight(Flight):
    def __init__(self, flight_id, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats, in_state=True):
        super().__init__(flight_id, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats)
        self.in_state = in_state

    def domestic_details(self):
        print(f"Domestic Flight {self.flight_number} - {'Within State' if self.in_state else 'Inter-State'}")


# International Flight (inherits from Flight)
class InternationalFlight(Flight):
    def __init__(self, flight_id, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats, passport_required=True):
        super().__init__(flight_id, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats)
        self.passport_required = passport_required

    def international_details(self):
        print(f"International Flight {self.flight_number} - {'Passport Required' if self.passport_required else 'Passport Not Required'}")


# -------- Example Usage --------
if __name__ == "__main__":
    # Create flights
    domestic_flight = DomesticFlight(101, "AI-202", "Mumbai", "Delhi", "2025-09-01 08:00", "2025-09-01 10:00", 3)
    international_flight = InternationalFlight(202, "AI-909", "Delhi", "New York", "2025-09-05 23:00", "2025-09-06 09:00", 2)

    # Show flight details
    domestic_flight.flight_details()
    international_flight.flight_details()

    # Booking seats
    domestic_flight.book_seat("Sumit")
    domestic_flight.book_seat("Karan")
    domestic_flight.book_seat("Candhani")
    domestic_flight.book_seat("Dravid")   # No seats left

    # Cancel reservation
    domestic_flight.cancel_reservation("Karan")  # No reservation found
    domestic_flight.book_seat("Dravid")   # Now David can book

    # Show details again
    domestic_flight.flight_details()

    # Specific details
    domestic_flight.domestic_details()
    international_flight.international_details()




# ## Output:
# Flight AI-202 (ID: 101)
# Route: Mumbai → Delhi
# Departure: 2025-09-01 08:00, Arrival: 2025-09-01 10:00
# Available Seats: 3
# ----------------------------------------
# Flight AI-909 (ID: 202)
# Route: Delhi → New York
# Departure: 2025-09-05 23:00, Arrival: 2025-09-06 09:00
# Available Seats: 2
# ----------------------------------------
# Seat booked successfully for Sumit on flight AI-202.
# Seat booked successfully for Karan on flight AI-202.
# Seat booked successfully for Candhani on flight AI-202.
# No seats available!
# Reservation for Karan on flight AI-202 has been cancelled.
# Seat booked successfully for Dravid on flight AI-202.
# Flight AI-202 (ID: 101)
# Route: Mumbai → Delhi
# Departure: 2025-09-01 08:00, Arrival: 2025-09-01 10:00
# Available Seats: 0
# ----------------------------------------
# Domestic Flight AI-202 - Within State
# International Flight AI-909 - Passport Required