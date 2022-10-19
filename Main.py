# Author: Bradley Peters
# StudentID: 001423299

from Objects.Package import Package
from Objects.Truck import Truck
from Utils.DeliveryAlgorithm import deliver_packages_for_truck
from Utils.HashMap import HashMap
from Utils.InterfaceUtils import start_interface
from Utils.PackageUtils import get_packages


class Main:
    # Initialize variables
    packages = get_packages()
    packages_map = HashMap()

    # Populate Packages Map
    for p in packages:  # type: Package
        packages_map.add(p.id, p)

    # Load Packages
    # Initial manual load
    truck1_packages = [1, 2, 3, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck2_packages = [4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 25, 28, 32, 36, 38]
    truck3_packages = [17, 21, 22, 23, 24, 26, 27, 33, 35, 39]

    truck1: Truck = Truck(1, "4001 South 700 East", 16, "8:00", None, 0.0, truck1_packages, 18)
    truck2: Truck = Truck(2, "4001 South 700 East", 16, "9:05", None, 0.0, truck2_packages, 18)

    # Deliver packages
    deliver_packages_for_truck(truck1, packages_map)
    deliver_packages_for_truck(truck2, packages_map)

    # Wait until at least one driver is back to get 3rd truck.
    departure_time = min(truck1.time, truck2.time)
    departure_time = '{}:{}'.format(departure_time.hour, departure_time.minute)
    truck3: Truck = Truck(3, "4001 South 700 East", 16, departure_time, None, 0.0, truck3_packages, 18)
    deliver_packages_for_truck(truck3, packages_map)

    # Start interface
    start_interface(truck1, truck2, truck3, packages_map)
