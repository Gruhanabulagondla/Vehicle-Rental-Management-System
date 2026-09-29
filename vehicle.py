vehicles = {
    1: {
        "name": "Maruti Swift",
        "type": "Car",
        "rate": 1200,
        "available": True
    },
    2: {
        "name": "Hyundai Creta",
        "type": "SUV",
        "rate": 1800,
        "available": True
    },
    3: {
        "name": "Royal Enfield Classic",
        "type": "Bike",
        "rate": 700,
        "available": True
    },
    4: {
        "name": "Honda Activa",
        "type": "Scooter",
        "rate": 400,
        "available": True
    },
    5: {
        "name": "Toyota Innova",
        "type": "MPV",
        "rate": 2200,
        "available": True
    }
}

rentals = {}
rental_id = 1001


def display_vehicles():
    print("\n========== VEHICLE LIST ==========")

    print(
        f"{'No.':<5}"
        f"{'Vehicle':<25}"
        f"{'Type':<12}"
        f"{'Rate/Day':<12}"
        f"{'Status'}"
    )

    print("-" * 70)

    for number, vehicle in vehicles.items():

        if vehicle["available"]:
            status = "Available"
        else:
            status = "Rented"

        print(
            f"{number:<5}"
            f"{vehicle['name']:<25}"
            f"{vehicle['type']:<12}"
            f"₹{vehicle['rate']:<11}"
            f"{status}"
        )


def search_vehicle():
    search_type = input("\nEnter vehicle type: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for number, vehicle in vehicles.items():

        if vehicle["type"].lower() == search_type:

            status = "Available" if vehicle["available"] else "Rented"

            print(f"\nVehicle Number: {number}")
            print(f"Vehicle: {vehicle['name']}")
            print(f"Type: {vehicle['type']}")
            print(f"Rate per Day: ₹{vehicle['rate']}")
            print(f"Status: {status}")

            found = True

    if not found:
        print("No vehicles found for this type.")


def rent_vehicle():
    global rental_id

    display_vehicles()

    try:
        vehicle_number = int(input("\nEnter vehicle number: "))

        if vehicle_number not in vehicles:
            print("Invalid vehicle number.")
            return

        vehicle = vehicles[vehicle_number]

        if not vehicle["available"]:
            print("Sorry! This vehicle is already rented.")
            return

        customer_name = input("Enter customer name: ").strip()

        if not customer_name:
            print("Customer name cannot be empty.")
            return

        phone = input("Enter phone number: ").strip()

        if not phone.isdigit() or len(phone) != 10:
            print("Enter a valid 10-digit phone number.")
            return

        days = int(input("Enter number of rental days: "))

        if days <= 0:
            print("Rental days must be greater than 0.")
            return

        total_amount = vehicle["rate"] * days

        current_rental_id = rental_id
        rental_id += 1

        rentals[current_rental_id] = {
            "customer": customer_name,
            "phone": phone,
            "vehicle_number": vehicle_number,
            "vehicle": vehicle["name"],
            "days": days,
            "rate": vehicle["rate"],
            "total": total_amount
        }

        vehicle["available"] = False

        print("\n========== RENTAL SUCCESSFUL ==========")
        print(f"Rental ID: {current_rental_id}")
        print(f"Customer: {customer_name}")
        print(f"Phone: {phone}")
        print(f"Vehicle: {vehicle['name']}")
        print(f"Rental Days: {days}")
        print(f"Rate Per Day: ₹{vehicle['rate']}")
        print(f"Total Amount: ₹{total_amount}")

    except ValueError:
        print("Please enter valid numbers.")


def view_rentals():
    print("\n========== ACTIVE RENTALS ==========")

    if not rentals:
        print("No active rentals.")
        return

    for rental_id, rental in rentals.items():

        print(f"\nRental ID: {rental_id}")
        print(f"Customer: {rental['customer']}")
        print(f"Phone: {rental['phone']}")
        print(f"Vehicle: {rental['vehicle']}")
        print(f"Rental Days: {rental['days']}")
        print(f"Rate Per Day: ₹{rental['rate']}")
        print(f"Total Amount: ₹{rental['total']}")


def return_vehicle():
    try:
        rental_number = int(input("\nEnter rental ID: "))

        if rental_number not in rentals:
            print("Rental ID not found.")
            return

        rental = rentals[rental_number]

        vehicle_number = rental["vehicle_number"]

        vehicles[vehicle_number]["available"] = True

        print("\n========== VEHICLE RETURN ==========")
        print(f"Rental ID: {rental_number}")
        print(f"Customer: {rental['customer']}")
        print(f"Vehicle: {rental['vehicle']}")
        print(f"Amount Paid: ₹{rental['total']}")

        del rentals[rental_number]

        print("\nVehicle returned successfully.")

    except ValueError:
        print("Please enter a valid rental ID.")


def main():
    print("========== VEHICLE RENTAL MANAGEMENT SYSTEM ==========")

    while True:

        print("\n1. View Vehicles")
        print("2. Search Vehicle")
        print("3. Rent Vehicle")
        print("4. View Active Rentals")
        print("5. Return Vehicle")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_vehicles()

        elif choice == "2":
            search_vehicle()

        elif choice == "3":
            rent_vehicle()

        elif choice == "4":
            view_rentals()

        elif choice == "5":
            return_vehicle()

        elif choice == "6":
            print("\nThank you for using Vehicle Rental Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()