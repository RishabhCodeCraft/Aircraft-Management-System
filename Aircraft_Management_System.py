class Aircraft:
    def __init__(self, tail_number, model, capacity, status="Available"):
        self.tail_number = tail_number
        self.model = model
        self.capacity = capacity
        self.status = status

    def __str__(self):
        return f"Aircraft {self.tail_number}: {self.model} (Capacity: {self.capacity}, Status: {self.status})"

    def change_status(self, new_status):
        self.status = new_status

class Fleet:
    def __init__(self):
        self.aircraft = {}

    def add_aircraft(self, aircraft):
        self.aircraft[aircraft.tail_number] = aircraft

    def remove_aircraft(self, tail_number):
        if tail_number in self.aircraft:
            del self.aircraft[tail_number]
            return True
        return False

    def get_aircraft(self, tail_number):
        return self.aircraft.get(tail_number)

    def list_aircraft(self):
        for aircraft in self.aircraft.values():
            print(aircraft)

    def available_aircraft(self):
        return [aircraft for aircraft in self.aircraft.values() if aircraft.status == "Available"]

# Example usage
fleet = Fleet()

# Add some aircraft
fleet.add_aircraft(Aircraft("N12345", "Boeing 737", 180))
fleet.add_aircraft(Aircraft("N67890", "Airbus A320", 150))
fleet.add_aircraft(Aircraft("N87233", "Airbus A321neo", 150))
fleet.add_aircraft(Aircraft("N68453", "Airbus A330", 300))
fleet.add_aircraft(Aircraft("N23784", "Boeing 777", 350))
fleet.add_aircraft(Aircraft("N28975", "Boeing 787", 350))
fleet.add_aircraft(Aircraft("N12786", "Embraer E175", 76))

# List all aircraft
print("All aircraft:")
fleet.list_aircraft()

# Change status of an aircraft
aircraft = fleet.get_aircraft("N12345")
if aircraft:
    aircraft.change_status("In Maintenance")

# List available aircraft
print("\nAvailable aircraft:")
for aircraft in fleet.available_aircraft():
    print(aircraft)

# Remove an aircraft
fleet.remove_aircraft("N67890")

# List all aircraft again
print("\nUpdated aircraft list:")
fleet.list_aircraft()