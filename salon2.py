from datetime import datetime, timedelta  # Import necessary modules for date and time handling
from typing import List  # Import List type from typing module for type hints

class Service:
    def __init__(self, name: str, masters: List[str]):
        # Initialize a Service object with a name and list of masters
        self.name = name
        self.masters = masters

    def get_name(self) -> str:
        # Method to get the name of the service as a string
        return self.name

    def get_masters(self) -> List[str]:
        # Method to get the list of masters specializing in this service
        return self.masters

    def get_details(self) -> str:
        # Method to get details of the service as a string
        return f"Service: {self.name}, Masters: {', '.join(self.masters)}"

class BeautySalon:
    def __init__(self):
        # Initialize BeautySalon object with empty lists for services and employees
        self.services = []
        self.employees = []

    def add_service(self, service: Service):
        # Method to add a new service to the salon's list of services
        self.services.append(service)

    def add_employee(self, employee):
        # Method to add a new employee to the salon's list of employees
        self.employees.append(employee)

    def get_available_times(self, service_name: str, date: datetime, master: str) -> List[datetime]:
        # Method to get available time slots for booking a service with a specific master on a given date
        available_times = []
        for service in self.services:
            if service.get_name() == service_name and master in service.get_masters():
                current_time = datetime(date.year, date.month, date.day, 9, 0)
                while current_time.hour < 17:
                    available_times.append(current_time)
                    current_time += timedelta(hours=1)
                break
        return available_times

    def book_appointment(self, client_name: str, service_name: str, date_time: datetime, master: str) -> str:
        # Method to book an appointment for a client at a specified date and time with a selected master and service
        return f"Appointment booked for {client_name} on {date_time.strftime('%Y-%m-%d %H:%M')} with {master} for {service_name}"

class ManicureService(Service):
    def __init__(self, masters: List[str]):
        # Initialize ManicureService object as a subclass of Service for manicure service
        super().__init__("Manicure", masters)

class PedicureService(Service):
    def __init__(self, masters: List[str]):
        # Initialize PedicureService object as a subclass of Service for pedicure service
        super().__init__("Pedicure", masters)

class MakeupService(Service):
    def __init__(self, masters: List[str]):
        # Initialize MakeupService object as a subclass of Service for makeup service
        super().__init__("Makeup", masters)

class HairStylingService(Service):
    def __init__(self, masters: List[str]):
        # Initialize HairStylingService object as a subclass of Service for hair styling service
        super().__init__("Hair Styling", masters)

class EyelashBrowLaminationService(Service):
    def __init__(self, masters: List[str]):
        # Initialize EyelashBrowLaminationService object as a subclass of Service for eyelash & brow lamination service
        super().__init__("Eyelash & Brow Lamination", masters)

def main():
    # Main function to interact with the user
    print("Welcome to our Beauty Salon!")
    beauty_salon = BeautySalon()  # Create an instance of the BeautySalon

    # Add different services with their respective masters to the beauty salon
    beauty_salon.add_service(ManicureService(["Ayaulym", "Zhanna", "Tomiris"]))
    beauty_salon.add_service(PedicureService(["Aidana", "Zhasmin", "Anel"]))
    beauty_salon.add_service(MakeupService(["Ainara", "Gulya", "Erke"]))
    beauty_salon.add_service(HairStylingService(["Lola", "Aya", "Marziya"]))
    beauty_salon.add_service(EyelashBrowLaminationService(["Laura", "Sophiya", "Zaure"]))

    client_name = input("Your Name: ")  # Prompt user to enter their name
    print("Choose Service:")
    for i, service in enumerate(beauty_salon.services):
        print(f"{i + 1}. {service.get_name()}")  # Display service options to the user
    service_choice = int(input()) - 1  # Get user's choice of service
    print("Choose Master:")
    for i, master in enumerate(beauty_salon.services[service_choice].get_masters()):
        print(f"{i + 1}. {master}")  # Display master options for the chosen service
    master_choice = int(input()) - 1  # Get user's choice of master

    try:
        date_str = input("Choose Date (YYYY-MM-DD): ")  # Prompt user to enter appointment date
        date = datetime.strptime(date_str, "%Y-%m-%d")  # Convert input date string to datetime object
        time_str = input("Choose Time (HH:MM): ")  # Prompt user to enter appointment time
        time = datetime.strptime(time_str, "%H:%M")  # Convert input time string to datetime object
        date_time = datetime(date.year, date.month, date.day, time.hour, time.minute)  # Create datetime object for the appointment date and time

        # Get available appointment times for the chosen service, date, and master
        available_times = beauty_salon.get_available_times(beauty_salon.services[service_choice].get_name(), date, beauty_salon.services[service_choice].get_masters()[master_choice])

        if date_time in available_times:
            # If the chosen date and time is available, book the appointment
            appointment_info = beauty_salon.book_appointment(client_name, beauty_salon.services[service_choice].get_name(), date_time, beauty_salon.services[service_choice].get_masters()[master_choice])
            print(f"Appointment booked for {client_name} on {date_time.strftime('%Y-%m-%d %H:%M')} with {beauty_salon.services[service_choice].get_masters()[master_choice]} for {beauty_salon.services[service_choice].get_name()}")
        else:
            # If the chosen date and time is not available, inform the user
            print("Selected time is not available for this service, master, and date.")
    except ValueError:
        print("Please enter valid date and time.")  # Handle invalid date and time input

if __name__ == "__main__":
    while True:
        # Continuously run the main function to manage appointments
        main()

        a = input("Do you need additional appointment? (Yes/No): ")  # Ask user if they need another appointment
        if a.lower() == "yes":
            continue  # Continue with another appointment if requested
        elif a.lower() == "no":
            break  # Exit the loop and end the program if not requested
        else:
            print("Invalid input")  # Display error message for invalid input
            break  # Exit the loop and end the program
