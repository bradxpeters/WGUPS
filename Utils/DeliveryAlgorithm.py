from datetime import timedelta
from typing import Optional

from Objects.Package import Package
from Objects.Truck import Truck
from Utils.DistanceUtils import distance_between_truck_and_package
from Utils.HashMap import HashMap


def deliver_packages_for_truck(truck: Truck, packages_map: HashMap):
    packages_to_deliver = []
    # O(n)
    for package_id in truck.packages:
        package = packages_map.get(package_id)  # O(1)
        packages_to_deliver.append(package)  # O(1)

    # O(1)
    truck.packages.clear()

    # O(n^2)
    while len(packages_to_deliver) > 0:
        next_address_distance = 1000
        next_package: Optional[Package] = None

        # O(n)
        for package in packages_to_deliver:  # type: Package
            distance = distance_between_truck_and_package(truck, package)
            if distance <= next_address_distance:
                next_address_distance = distance
                next_package = package

        # O(1)
        truck.packages.append(next_package.id)

        # O(1)
        packages_to_deliver.remove(next_package)

        # O(1)
        truck.mileage += next_address_distance

        # O(1)
        truck.address = next_package.address

        # O(1)
        truck.time += timedelta(hours=next_address_distance / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.departure_time
