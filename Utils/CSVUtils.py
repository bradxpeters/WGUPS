import csv


def get_addresses_from_csv() -> list:
    with open("Resources/addresses.csv") as addresses_csv:
        addresses = csv.reader(addresses_csv)
        address_list = list(addresses)
    return address_list


def get_distances_from_csv() -> list:
    with open("Resources/distances.csv") as distances_csv:
        distances = csv.reader(distances_csv)
        distance_list = list(distances)
    return distance_list


def get_packages_from_csv() -> list:
    with open("Resources/packages.csv") as packages_csv:
        packages = csv.reader(packages_csv)
        package_list = list(packages)
    return package_list
