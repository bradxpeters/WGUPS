from Objects.Package import Package
from Objects.Truck import Truck
from Utils.AddressUtils import get_address
from Utils.CSVUtils import get_distances_from_csv


def distance_between_truck_and_package(truck: Truck, package: Package) -> float:
    x = get_address(truck.address)
    y = get_address(package.address)
    distances = get_distances_from_csv()
    distance = distances[y][x]

    if distance == '':
        distance = distances[x][y]

    if distance == '':
        print("No distance could be found for ", truck.address, " and ", package.address)

    return float(distance)
