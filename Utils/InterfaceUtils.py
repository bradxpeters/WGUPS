from time import strptime

from Objects.Truck import Truck


def start_interface(truck1: Truck, truck2: Truck, truck3: Truck, packages_map):
    print("Western Governors University Parcel Service (WGUPS)")
    print("The total mileage for today's routes were: ")
    print(truck1.mileage + truck2.mileage + truck3.mileage)

    print("[Truck 1] Departed:",
          truck1.departure_time.time(),
          "Returned:",
          truck1.time.time(),
          "Delivered:",
          len(truck1.packages)
          )

    print("[Truck 2] Departed:",
          truck2.departure_time.time(),
          "Returned:",
          truck2.time.time(),
          "Delivered:",
          len(truck2.packages)
          )

    print("[Truck 3] Departed:",
          truck3.departure_time.time(),
          "Returned:",
          truck3.time.time(),
          "Delivered:",
          len(truck3.packages)
          )

    try:
        user_time = input("Enter a time using 24 hour time format: HH:MM:SS\n")
        new_time = strptime(user_time, '%H:%M:%S')

        print("Select an option below:")
        print("1. Show the status of a single package")
        print("2. Show the status of all packages")

        selection = input("Enter selection number\n")

        if selection == '1':
            try:
                package_id = input("Enter the package id\n")
                package = packages_map.get(int(package_id))
                package.get_status(new_time)
                print(package)
            except ValueError:
                print("Couldn't find package, exiting...")
                exit()

        elif selection == '2':
            try:
                for package_id in range(1, 41):
                    package = packages_map.get(package_id)
                    package.get_status(new_time)
                    print(package)
            except ValueError:
                print("Error fetching all package statuses")
                exit()
        else:
            exit()
    except ValueError:
        print("Invalid choice, exiting...")
        exit()
