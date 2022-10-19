from datetime import timedelta
from typing import Optional

from Objects.Package import Package
from Objects.Truck import Truck
from Utils.DistanceUtils import distance_between_truck_and_package
from Utils.HashMap import HashMap


def deliver_packages_for_truck(truck: Truck, packages_map: HashMap):
    packages_to_deliver = []
    for package_id in truck.packages:
        package = packages_map.get(package_id)
        packages_to_deliver.append(package)

    truck.packages.clear()

    while len(packages_to_deliver) > 0:
        next_address_distance = 10000
        next_package: Optional[Package] = None

        for package in packages_to_deliver:  # type: Package
            if distance_between_truck_and_package(truck, package) <= next_address_distance:
                next_address_distance = distance_between_truck_and_package(truck, package)
                next_package = package

        truck.packages.append(next_package.id)

        packages_to_deliver.remove(next_package)

        truck.mileage += next_address_distance

        truck.address = next_package.address

        truck.time += timedelta(hours=next_address_distance / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.departure_time
