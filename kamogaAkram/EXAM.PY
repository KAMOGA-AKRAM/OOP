import logging
from collections import deque
from itertools import cycle

# Setup logging configuration for info messages
logging.basicConfig(level=logging.INFO, format='%(message)s')


class Courier:
    """Represents a delivery person named '60seconds' who handles package deliveries."""

    def __init__(self, name="60seconds"):
        self.name = name
        self.packages = deque()  # Queue of packages: (description, destination, recipient)

    def assign(self, package):
        """Assign a package and notify the recipient immediately."""
        self.packages.append(package)
        print(f"Message to {package[2]}: Your package '{package[0]}' will be delivered soon by {self.name}!")

    def deliver(self):
        """Deliver all packages in the queue."""
        if not self.packages:
            print("No packages to deliver.")
            return
        while self.packages:
            desc, dest, recipient = self.packages.popleft()
            print(f"{self.name} delivered '{desc}' to {dest} for {recipient}")
            logging.info(f"Delivered '{desc}' to {dest} for {recipient}")


def hostel_route(hostels):
    """Create an infinite cycling iterator over the hostels."""
    return cycle(hostels)


def main():
    courier = Courier()
    hostels = ['CERAMEK', 'SKY', 'DAVIDS ARK']
    route = hostel_route(hostels)

    menu = (
        "\nMenu:\n"
        "1. List hostels\n"
        "2. Add package\n"
        "3. Deliver packages\n"
        "4. Next hostel on route\n"
        "5. Exit"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == '1':
            print("Hostels on the route:", ", ".join(hostels))
        elif choice == '2':
            desc = input("Package description: ").strip()
            dest = input("Destination hostel: ").strip().upper()
            recipient = input("Recipient name: ").strip()
            if dest not in hostels:
                print(f"Oops, '{dest}' is not on the delivery route. Try again.")
                continue
            courier.assign((desc, dest, recipient))
        elif choice == '3':
            courier.deliver()
        elif choice == '4':
            next_hostel = next(route)
            print(f"Next hostel on the delivery route: {next_hostel}")
        elif choice == '5':
            print("Goodbye! Have a great day.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
